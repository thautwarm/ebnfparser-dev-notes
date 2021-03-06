# This file is automatically generated by EBNFParser.
from Ruikowa.ObjectRegex.Tokenizer import unique_literal_cache_pool, regex_matcher, char_matcher, str_matcher, Tokenizer
from Ruikowa.ObjectRegex.Node import AstParser, Ref, SeqParser, LiteralValueParser as L, LiteralNameParser, Undef
namespace = globals()
recur_searcher = set()
token_table = ((unique_literal_cache_pool["space"], regex_matcher('\s+')),
               (unique_literal_cache_pool["number"], regex_matcher('\d+')),
               (unique_literal_cache_pool["auto_const"], char_matcher(('.', '-', '+', ')', '('))),
               (unique_literal_cache_pool["auto_const"], str_matcher(('//', '**'))),
               (unique_literal_cache_pool["auto_const"], char_matcher(('/', '*'))))

class UNameEnum:
# names

    space = unique_literal_cache_pool['space']
    number = unique_literal_cache_pool['number']
    decimal = unique_literal_cache_pool['decimal']
    atom = unique_literal_cache_pool['atom']
    factor = unique_literal_cache_pool['factor']
    power = unique_literal_cache_pool['power']
    mulDiv = unique_literal_cache_pool['mulDiv']
    arith = unique_literal_cache_pool['arith']
        
cast_map = {}
token_func = lambda _: Tokenizer.from_raw_strings(_, token_table, ({"space"}, {}),cast_map=cast_map)
space = LiteralNameParser('space')
number = LiteralNameParser('number')
decimal = AstParser([Ref('number'), SeqParser(['.', Ref('number')], at_least=0,at_most=1)],
                    name="decimal",
                    to_ignore=({}, {}))
atom = AstParser([Ref('decimal')],
                 ['(', Ref('arith'), ')'],
                 name="atom",
                 to_ignore=({}, {}))
factor = AstParser([SeqParser(['-'], ['+'], at_least=0,at_most=1), Ref('atom')],
                   name="factor",
                   to_ignore=({}, {}))
power = AstParser([Ref('factor'), SeqParser(['**', Ref('factor')], at_least=0,at_most=Undef)],
                  name="power",
                  to_ignore=({}, {}))
mulDiv = AstParser([Ref('power'), SeqParser(['//', Ref('power')], ['/', Ref('power')], ['*', Ref('power')], at_least=0,at_most=Undef)],
                   name="mulDiv",
                   to_ignore=({}, {}))
arith = AstParser([Ref('mulDiv'), SeqParser(['+', Ref('mulDiv')], ['-', Ref('mulDiv')], at_least=0,at_most=Undef)],
                  name="arith",
                  to_ignore=({}, {}))
arith.compile(namespace, recur_searcher)