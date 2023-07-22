# Generated from /home/needslyp/labs/sem6/YAPIS/yapsi_python/file.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fileParser import fileParser
else:
    from fileParser import fileParser

# This class defines a complete listener for a parse tree produced by fileParser.
class fileListener(ParseTreeListener):

    # Enter a parse tree produced by fileParser#program.
    def enterProgram(self, ctx:fileParser.ProgramContext):
        pass

    # Exit a parse tree produced by fileParser#program.
    def exitProgram(self, ctx:fileParser.ProgramContext):
        pass


    # Enter a parse tree produced by fileParser#stat.
    def enterStat(self, ctx:fileParser.StatContext):
        pass

    # Exit a parse tree produced by fileParser#stat.
    def exitStat(self, ctx:fileParser.StatContext):
        pass


    # Enter a parse tree produced by fileParser#def.
    def enterDef(self, ctx:fileParser.DefContext):
        pass

    # Exit a parse tree produced by fileParser#def.
    def exitDef(self, ctx:fileParser.DefContext):
        pass


    # Enter a parse tree produced by fileParser#return.
    def enterReturn(self, ctx:fileParser.ReturnContext):
        pass

    # Exit a parse tree produced by fileParser#return.
    def exitReturn(self, ctx:fileParser.ReturnContext):
        pass


    # Enter a parse tree produced by fileParser#parameter.
    def enterParameter(self, ctx:fileParser.ParameterContext):
        pass

    # Exit a parse tree produced by fileParser#parameter.
    def exitParameter(self, ctx:fileParser.ParameterContext):
        pass


    # Enter a parse tree produced by fileParser#op.
    def enterOp(self, ctx:fileParser.OpContext):
        pass

    # Exit a parse tree produced by fileParser#op.
    def exitOp(self, ctx:fileParser.OpContext):
        pass


    # Enter a parse tree produced by fileParser#s_op.
    def enterS_op(self, ctx:fileParser.S_opContext):
        pass

    # Exit a parse tree produced by fileParser#s_op.
    def exitS_op(self, ctx:fileParser.S_opContext):
        pass


    # Enter a parse tree produced by fileParser#comp.
    def enterComp(self, ctx:fileParser.CompContext):
        pass

    # Exit a parse tree produced by fileParser#comp.
    def exitComp(self, ctx:fileParser.CompContext):
        pass


    # Enter a parse tree produced by fileParser#expr.
    def enterExpr(self, ctx:fileParser.ExprContext):
        pass

    # Exit a parse tree produced by fileParser#expr.
    def exitExpr(self, ctx:fileParser.ExprContext):
        pass


    # Enter a parse tree produced by fileParser#for_cycle.
    def enterFor_cycle(self, ctx:fileParser.For_cycleContext):
        pass

    # Exit a parse tree produced by fileParser#for_cycle.
    def exitFor_cycle(self, ctx:fileParser.For_cycleContext):
        pass


    # Enter a parse tree produced by fileParser#while_cycle.
    def enterWhile_cycle(self, ctx:fileParser.While_cycleContext):
        pass

    # Exit a parse tree produced by fileParser#while_cycle.
    def exitWhile_cycle(self, ctx:fileParser.While_cycleContext):
        pass


    # Enter a parse tree produced by fileParser#if_else.
    def enterIf_else(self, ctx:fileParser.If_elseContext):
        pass

    # Exit a parse tree produced by fileParser#if_else.
    def exitIf_else(self, ctx:fileParser.If_elseContext):
        pass


    # Enter a parse tree produced by fileParser#list.
    def enterList(self, ctx:fileParser.ListContext):
        pass

    # Exit a parse tree produced by fileParser#list.
    def exitList(self, ctx:fileParser.ListContext):
        pass


    # Enter a parse tree produced by fileParser#iter.
    def enterIter(self, ctx:fileParser.IterContext):
        pass

    # Exit a parse tree produced by fileParser#iter.
    def exitIter(self, ctx:fileParser.IterContext):
        pass


    # Enter a parse tree produced by fileParser#func.
    def enterFunc(self, ctx:fileParser.FuncContext):
        pass

    # Exit a parse tree produced by fileParser#func.
    def exitFunc(self, ctx:fileParser.FuncContext):
        pass


    # Enter a parse tree produced by fileParser#stat_box.
    def enterStat_box(self, ctx:fileParser.Stat_boxContext):
        pass

    # Exit a parse tree produced by fileParser#stat_box.
    def exitStat_box(self, ctx:fileParser.Stat_boxContext):
        pass



del fileParser