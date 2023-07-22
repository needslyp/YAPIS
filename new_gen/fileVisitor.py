# Generated from /home/needslyp/labs/sem6/YAPIS/yapsi_python/file.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fileParser import fileParser
else:
    from fileParser import fileParser

# This class defines a complete generic visitor for a parse tree produced by fileParser.

class fileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fileParser#program.
    def visitProgram(self, ctx:fileParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#stat.
    def visitStat(self, ctx:fileParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#def.
    def visitDef(self, ctx:fileParser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#return.
    def visitReturn(self, ctx:fileParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#parameter.
    def visitParameter(self, ctx:fileParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#op.
    def visitOp(self, ctx:fileParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#s_op.
    def visitS_op(self, ctx:fileParser.S_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#comp.
    def visitComp(self, ctx:fileParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#expr.
    def visitExpr(self, ctx:fileParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#for_cycle.
    def visitFor_cycle(self, ctx:fileParser.For_cycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#while_cycle.
    def visitWhile_cycle(self, ctx:fileParser.While_cycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#if_else.
    def visitIf_else(self, ctx:fileParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#list.
    def visitList(self, ctx:fileParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#iter.
    def visitIter(self, ctx:fileParser.IterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#func.
    def visitFunc(self, ctx:fileParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fileParser#stat_box.
    def visitStat_box(self, ctx:fileParser.Stat_boxContext):
        return self.visitChildren(ctx)



del fileParser