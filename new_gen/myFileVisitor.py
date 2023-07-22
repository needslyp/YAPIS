import copy
import re

from new_gen.fileVisitor import *
from new_gen.fileParser import fileParser

class MyErrorVisitor(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_msg(self):
        print(self.msg)

class MyFileVisitor(fileVisitor):
        output = """"""

        def writeToFile(self):
            f = open('my_code.py', 'w')
            f.write(self.output)

            f.write('\n\nmain()\n')
            f.close()

        def printOutput(self):
            print(self.output)
        def getEnv(self, ctx):
            curCtx = ctx
            while (not (isinstance(curCtx, fileParser.DefContext) or
                        isinstance(curCtx, fileParser.Stat_boxContext) or
                        isinstance(curCtx, fileParser.ProgramContext) or
                        isinstance(curCtx, fileParser.For_cycleContext)
            ) and ctx):
                curCtx = curCtx.parentCtx
            return curCtx

        def getCount(self, ctx):
            curCtx = ctx
            count = -1
            while (not (isinstance(curCtx, fileParser.ProgramContext)
            ) and ctx):
                curCtx = curCtx.parentCtx
                if (not (isinstance(curCtx, fileParser.Stat_boxContext)
                        or isinstance(curCtx, fileParser.For_cycleContext)
                        or isinstance(curCtx, fileParser.While_cycleContext))):
                    count += 1
            return count

        def existsVar(self, ctx = fileParser.ProgramContext, name = '', type = 'def'):
            curCtx = self.getEnv(ctx)
            while curCtx:
                if curCtx.env.get(name):
                    if curCtx.env[name]['type'] == type or type == '*':
                        return 1
                    return -1
                curCtx = self.getEnv(curCtx.parentCtx)
            return 0

        # Visit a parse tree produced by fileParser#program.
        def visitProgram(self, ctx: fileParser.ProgramContext):
            ctxEnv = self.getEnv(ctx)
            ctxEnv.env = {}
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#stat.
        def visitStat(self, ctx: fileParser.StatContext):
            pCtx = self.getEnv(ctx)
            count = self.getCount(ctx)
            if ctx.ID() and ctx.EQ() and ctx.expr():
                nameID = ctx.ID(0).getText()
                # print(nameID)
                expr = ctx.expr(0).getText()
                # print(expr)
                tab = count * '    '
                self.output += f'{tab}{nameID} = {expr}\n'



            if not ctx.ID() and ctx.expr():
                expr = ctx.expr(0).getText()
                # print(expr)
                tab = count * '    '
                self.output += f'{tab}{expr}\n'

            if ctx.ID():
                nameID = ctx.ID(0).getText()
                pCtx.env[nameID] = {'type': 'expr', 'ctx': ctx}

            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#def.
        def visitDef(self, ctx: fileParser.DefContext):
            pCtx = self.getEnv(ctx.parentCtx)
            count = self.getCount(ctx)

            funcName = ctx.ID().getText()
            params = []
            if type(ctx.parameter()) is list:
                for i in range(len(ctx.parameter())):
                    # print(ctx.parameter(i).TYPE().getText(), ctx.parameter(i).ID().getText())
                    params.append(ctx.parameter(i).ID().getText())

            tab = count * '    '
            self.output += f'{tab}def {funcName}({", ".join(params)}):\n'

            if self.existsVar(pCtx, funcName, 'def'):
                print(f'variable with this name already exists <{funcName}>')

            pCtx.env[funcName] = {'type': 'def', 'ctx': ctx}
            ctx.env = {}

            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#return.
        def visitReturn(self, ctx: fileParser.ReturnContext):
            pCtx = self.getEnv(ctx)
            tab = self.getCount(ctx) * '    '
            if ctx.expr():
                ID = ctx.expr().getText()
                self.output += f'{tab}return {ID}\n'

            if ctx.expr().ID():
                ID = ctx.expr().ID().getText()
                if self.existsVar(pCtx, ID, '*') != 1:
                    print(f'variable not exists <{ID}>')

            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#parameter.
        def visitParameter(self, ctx: fileParser.ParameterContext):
            pCtx = self.getEnv(ctx)

            name = ctx.ID().getText()
            type = ctx.TYPE().getText()

            if (not pCtx.env.get(name)):
                pCtx.env[name] = {'type': type, 'ctx': ctx}
            else:
                print('parameters must be unique')
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#op.
        def visitOp(self, ctx: fileParser.OpContext):
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#s_op.
        def visitS_op(self, ctx: fileParser.S_opContext):
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#comp.
        def visitComp(self, ctx: fileParser.CompContext):
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#expr.
        def visitExpr(self, ctx: fileParser.ExprContext):
            pCtx = self.getEnv(ctx)
            if ctx.ID():
                ID = ctx.ID().getText()
                if self.existsVar(pCtx, ID, '*') != 1:
                    if ID not in ['tree', 'left', 'right', 'queue']:
                        print(f'variable not exists <{ID}>')
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#for_cycle.
        def visitFor_cycle(self, ctx: fileParser.For_cycleContext):
            ctx.env = {}
            ID = ctx.ID(0).getText()
            expr = ctx.expr().getText()
            # print(ID, elem, expr)
            tab = (self.getCount(ctx)-1)*'    '
            self.output += f'{tab}for {ID} in {expr}:\n'

            ID = ctx.ID(0).getText()
            if ctx.ID(0).getText() != (ctx.ID(1).getText() or ctx.ID(2).getText):
                print(f'different variable')
            ctx.env[ID] = {'ctx': ctx.ID(0), 'type': ctx.TYPE()}

            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#while_cycle.
        def visitWhile_cycle(self, ctx: fileParser.While_cycleContext):
            ctx.env = {}
            ID = ctx.ID().getText()
            comp = ctx.comp().getText()
            elem = ctx.ELEMENT().getText()
            # print(ID, elem, expr)
            tab = (self.getCount(ctx) - 1) * '    '
            self.output += f'{tab}while ({ID} {comp} {elem}):\n'
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#if_else.
        def visitIf_else(self, ctx: fileParser.If_elseContext):
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#list.
        def visitList(self, ctx: fileParser.ListContext):
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#iter.
        def visitIter(self, ctx: fileParser.IterContext):
            pCtx = self.getEnv(ctx)
            if ctx.ID(1):
                ID = ctx.ID(1).getText()
                if self.existsVar(pCtx, ID, '*') != 1:
                    print(f'variable not exists <{ID}>')
            elif ctx.ELEMENT():
                ID = ctx.ELEMENT().getText()
                if self.existsVar(pCtx, ID, '*') != 1:
                    print(f'variable not exists <{ID}>')

            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#func.
        def visitFunc(self, ctx: fileParser.FuncContext):
            func = ctx.ID().getText()
            if not self.existsVar(ctx, func, 'def'):
                if func not in ['append', 'make_list', 'print', 'input', 'pop', 'len', 'balance', 'range']:
                    print(f'function not exists <{func}>')
            return self.visitChildren(ctx)

        # Visit a parse tree produced by fileParser#stat_box.
        def visitStat_box(self, ctx: fileParser.Stat_boxContext):
            ctx.env = {}
            return self.visitChildren(ctx)