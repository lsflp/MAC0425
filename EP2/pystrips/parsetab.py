
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME VARIABLE LPAREN RPAREN HYPHEN EQUALS DEFINE_KEY DOMAIN_KEY REQUIREMENTS_KEY STRIPS_KEY EQUALITY_KEY TYPING_KEY TYPES_KEY PREDICATES_KEY ACTION_KEY PARAMETERS_KEY PRECONDITION_KEY EFFECT_KEY AND_KEY NOT_KEY PROBLEM_KEY OBJECTS_KEY INIT_KEY GOAL_KEYpddl : domain\n            | problemdomain : LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPARENproblem : LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPARENdomain_def : LPAREN DOMAIN_KEY NAME RPARENproblem_def : LPAREN PROBLEM_KEY NAME RPARENobjects_def : LPAREN OBJECTS_KEY typed_constants_lst RPARENinit_def : LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN\n                | LPAREN INIT_KEY ground_predicates_lst RPARENgoal_def : LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPARENrequire_def : LPAREN REQUIREMENTS_KEY require_key_lst RPARENrequire_key_lst : require_key require_key_lst\n                       | require_keyrequire_key : STRIPS_KEY\n                   | EQUALITY_KEY\n                   | TYPING_KEYtypes_def : LPAREN TYPES_KEY names_lst RPARENpredicates_def : LPAREN PREDICATES_KEY predicate_def_lst RPARENpredicate_def_lst : predicate_def predicate_def_lst\n                         | predicate_defpredicate_def : LPAREN NAME typed_variables_lst RPAREN\n                     | LPAREN NAME RPARENaction_def_lst : action_def action_def_lst\n                      | action_defaction_def : LPAREN ACTION_KEY NAME parameters_def action_def_body RPARENparameters_def : PARAMETERS_KEY LPAREN typed_variables_lst RPAREN\n                      | PARAMETERS_KEY LPAREN RPARENaction_def_body : precond_def effects_defprecond_def : PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | PRECONDITION_KEY literaleffects_def : EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | EFFECT_KEY literalliterals_lst : literal literals_lst\n                    | literalliteral : LPAREN NOT_KEY predicate RPAREN\n               | predicateground_predicates_lst : ground_predicate ground_predicates_lst\n                             | ground_predicatepredicate : LPAREN NAME variables_lst RPAREN\n                 | LPAREN EQUALS VARIABLE VARIABLE RPAREN\n                 | LPAREN NAME RPARENground_predicate : LPAREN NAME constants_lst RPAREN\n                        | LPAREN NAME RPARENtyped_constants_lst : constants_lst HYPHEN type typed_constants_lst\n                           | constants_lst HYPHEN typetyped_variables_lst : variables_lst HYPHEN type typed_variables_lst\n                           | variables_lst HYPHEN typeconstants_lst : constant constants_lst\n                     | constantvariables_lst : VARIABLE variables_lst\n                     | VARIABLEnames_lst : NAME names_lst\n                 | NAMEtype : NAMEconstant : NAME'
    
_lr_action_items = {'HYPHEN':([35,37,38,52,83,86,94,],[50,-49,-55,-48,92,-51,-50,]),'TYPES_KEY':([21,],[34,]),'EQUALITY_KEY':([19,27,28,30,31,],[30,-14,-16,-15,30,]),'$end':([1,3,4,56,63,],[-2,-1,0,-4,-3,]),'PARAMETERS_KEY':([77,],[88,]),'EQUALS':([103,117,120,123,],[115,115,115,115,]),'AND_KEY':([53,73,103,117,],[68,82,113,127,]),'DEFINE_KEY':([2,],[5,]),'NAME':([11,12,22,34,37,38,48,50,53,58,62,66,67,69,70,92,103,117,120,123,],[17,18,38,48,38,-55,48,66,69,74,77,-54,38,38,69,66,114,114,114,114,]),'RPAREN':([17,18,27,28,29,30,31,36,37,38,40,43,45,47,48,49,52,54,55,59,60,61,64,66,67,69,71,74,75,78,79,80,81,84,85,86,89,90,91,93,94,97,98,100,101,104,105,107,108,110,111,114,116,119,121,122,124,125,128,129,131,132,133,134,135,],[25,26,-14,-16,42,-15,-13,51,-49,-55,56,-12,-24,63,-53,65,-48,-38,72,-20,76,-23,-52,-54,-45,80,-37,85,-19,-44,89,-43,90,93,-22,-51,99,-42,100,-21,-50,107,109,110,-47,-36,-28,-25,118,-10,-46,124,-32,128,-34,130,-41,131,-35,-33,-39,134,135,-40,-31,]),'REQUIREMENTS_KEY':([13,],[19,]),'NOT_KEY':([103,117,123,],[112,112,112,]),'VARIABLE':([66,74,86,98,101,114,115,126,],[-54,86,86,86,86,86,126,132,]),'DOMAIN_KEY':([7,9,],[11,11,]),'OBJECTS_KEY':([15,],[22,]),'LPAREN':([0,5,6,8,10,14,16,20,24,25,26,33,39,42,44,45,51,54,57,59,65,68,72,76,80,82,85,88,90,93,95,99,104,106,107,112,113,121,124,127,128,131,134,],[2,7,9,13,15,21,23,32,41,-5,-6,46,53,-11,58,46,-7,70,73,58,-17,70,-9,-18,-43,70,-22,98,-42,-21,103,-8,-36,117,-25,120,123,123,-41,123,-35,-39,-40,]),'GOAL_KEY':([41,],[57,]),'EFFECT_KEY':([96,102,104,124,128,130,131,134,],[106,-30,-36,-41,-35,-29,-39,-40,]),'PRECONDITION_KEY':([87,109,118,],[95,-27,-26,]),'STRIPS_KEY':([19,27,28,30,31,],[27,-14,-16,-15,27,]),'TYPING_KEY':([19,27,28,30,31,],[28,-14,-16,-15,28,]),'INIT_KEY':([23,],[39,]),'PREDICATES_KEY':([32,],[44,]),'ACTION_KEY':([46,],[62,]),'PROBLEM_KEY':([7,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'type':([50,92,],[67,101,]),'action_def':([33,45,],[45,45,]),'problem':([0,],[1,]),'precond_def':([87,],[96,]),'problem_def':([5,],[6,]),'require_def':([8,],[14,]),'parameters_def':([77,],[87,]),'objects_def':([10,],[16,]),'variables_lst':([74,86,98,101,114,],[83,94,83,83,125,]),'constants_lst':([22,37,67,69,],[35,52,35,81,]),'names_lst':([34,48,],[49,64,]),'pddl':([0,],[4,]),'init_def':([16,],[24,]),'ground_predicates_lst':([39,54,68,82,],[55,71,79,91,]),'predicates_def':([20,],[33,]),'literal':([95,106,113,121,127,],[102,116,121,121,121,]),'typed_variables_lst':([74,98,101,],[84,108,111,]),'typed_constants_lst':([22,67,],[36,78,]),'constant':([22,37,67,69,],[37,37,37,37,]),'predicate':([95,106,112,113,121,127,],[104,104,119,104,104,104,]),'predicate_def':([44,59,],[59,59,]),'action_def_lst':([33,45,],[47,61,]),'literals_lst':([113,121,127,],[122,129,133,]),'domain':([0,],[3,]),'predicate_def_lst':([44,59,],[60,75,]),'effects_def':([96,],[105,]),'goal_def':([24,],[40,]),'action_def_body':([87,],[97,]),'require_key_lst':([19,31,],[29,43,]),'types_def':([14,],[20,]),'ground_predicate':([39,54,68,82,],[54,54,54,54,]),'require_key':([19,31,],[31,31,]),'domain_def':([5,6,],[8,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pddl","S'",1,None,None,None),
  ('pddl -> domain','pddl',1,'p_pddl','parser.py',100),
  ('pddl -> problem','pddl',1,'p_pddl','parser.py',101),
  ('domain -> LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPAREN','domain',8,'p_domain','parser.py',106),
  ('problem -> LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPAREN','problem',8,'p_problem','parser.py',111),
  ('domain_def -> LPAREN DOMAIN_KEY NAME RPAREN','domain_def',4,'p_domain_def','parser.py',116),
  ('problem_def -> LPAREN PROBLEM_KEY NAME RPAREN','problem_def',4,'p_problem_def','parser.py',121),
  ('objects_def -> LPAREN OBJECTS_KEY typed_constants_lst RPAREN','objects_def',4,'p_objects_def','parser.py',126),
  ('init_def -> LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','init_def',7,'p_init_def','parser.py',131),
  ('init_def -> LPAREN INIT_KEY ground_predicates_lst RPAREN','init_def',4,'p_init_def','parser.py',132),
  ('goal_def -> LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','goal_def',7,'p_goal_def','parser.py',140),
  ('require_def -> LPAREN REQUIREMENTS_KEY require_key_lst RPAREN','require_def',4,'p_require_def','parser.py',145),
  ('require_key_lst -> require_key require_key_lst','require_key_lst',2,'p_require_key_lst','parser.py',150),
  ('require_key_lst -> require_key','require_key_lst',1,'p_require_key_lst','parser.py',151),
  ('require_key -> STRIPS_KEY','require_key',1,'p_require_key','parser.py',159),
  ('require_key -> EQUALITY_KEY','require_key',1,'p_require_key','parser.py',160),
  ('require_key -> TYPING_KEY','require_key',1,'p_require_key','parser.py',161),
  ('types_def -> LPAREN TYPES_KEY names_lst RPAREN','types_def',4,'p_types_def','parser.py',166),
  ('predicates_def -> LPAREN PREDICATES_KEY predicate_def_lst RPAREN','predicates_def',4,'p_predicates_def','parser.py',171),
  ('predicate_def_lst -> predicate_def predicate_def_lst','predicate_def_lst',2,'p_predicate_def_lst','parser.py',176),
  ('predicate_def_lst -> predicate_def','predicate_def_lst',1,'p_predicate_def_lst','parser.py',177),
  ('predicate_def -> LPAREN NAME typed_variables_lst RPAREN','predicate_def',4,'p_predicate_def','parser.py',185),
  ('predicate_def -> LPAREN NAME RPAREN','predicate_def',3,'p_predicate_def','parser.py',186),
  ('action_def_lst -> action_def action_def_lst','action_def_lst',2,'p_action_def_lst','parser.py',194),
  ('action_def_lst -> action_def','action_def_lst',1,'p_action_def_lst','parser.py',195),
  ('action_def -> LPAREN ACTION_KEY NAME parameters_def action_def_body RPAREN','action_def',6,'p_action_def','parser.py',203),
  ('parameters_def -> PARAMETERS_KEY LPAREN typed_variables_lst RPAREN','parameters_def',4,'p_parameters_def','parser.py',208),
  ('parameters_def -> PARAMETERS_KEY LPAREN RPAREN','parameters_def',3,'p_parameters_def','parser.py',209),
  ('action_def_body -> precond_def effects_def','action_def_body',2,'p_action_def_body','parser.py',217),
  ('precond_def -> PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN','precond_def',5,'p_precond_def','parser.py',222),
  ('precond_def -> PRECONDITION_KEY literal','precond_def',2,'p_precond_def','parser.py',223),
  ('effects_def -> EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN','effects_def',5,'p_effects_def','parser.py',231),
  ('effects_def -> EFFECT_KEY literal','effects_def',2,'p_effects_def','parser.py',232),
  ('literals_lst -> literal literals_lst','literals_lst',2,'p_literals_lst','parser.py',240),
  ('literals_lst -> literal','literals_lst',1,'p_literals_lst','parser.py',241),
  ('literal -> LPAREN NOT_KEY predicate RPAREN','literal',4,'p_literal','parser.py',249),
  ('literal -> predicate','literal',1,'p_literal','parser.py',250),
  ('ground_predicates_lst -> ground_predicate ground_predicates_lst','ground_predicates_lst',2,'p_ground_predicates_lst','parser.py',258),
  ('ground_predicates_lst -> ground_predicate','ground_predicates_lst',1,'p_ground_predicates_lst','parser.py',259),
  ('predicate -> LPAREN NAME variables_lst RPAREN','predicate',4,'p_predicate','parser.py',267),
  ('predicate -> LPAREN EQUALS VARIABLE VARIABLE RPAREN','predicate',5,'p_predicate','parser.py',268),
  ('predicate -> LPAREN NAME RPAREN','predicate',3,'p_predicate','parser.py',269),
  ('ground_predicate -> LPAREN NAME constants_lst RPAREN','ground_predicate',4,'p_ground_predicate','parser.py',279),
  ('ground_predicate -> LPAREN NAME RPAREN','ground_predicate',3,'p_ground_predicate','parser.py',280),
  ('typed_constants_lst -> constants_lst HYPHEN type typed_constants_lst','typed_constants_lst',4,'p_typed_constants_lst','parser.py',288),
  ('typed_constants_lst -> constants_lst HYPHEN type','typed_constants_lst',3,'p_typed_constants_lst','parser.py',289),
  ('typed_variables_lst -> variables_lst HYPHEN type typed_variables_lst','typed_variables_lst',4,'p_typed_variables_lst','parser.py',297),
  ('typed_variables_lst -> variables_lst HYPHEN type','typed_variables_lst',3,'p_typed_variables_lst','parser.py',298),
  ('constants_lst -> constant constants_lst','constants_lst',2,'p_constants_lst','parser.py',306),
  ('constants_lst -> constant','constants_lst',1,'p_constants_lst','parser.py',307),
  ('variables_lst -> VARIABLE variables_lst','variables_lst',2,'p_variables_lst','parser.py',315),
  ('variables_lst -> VARIABLE','variables_lst',1,'p_variables_lst','parser.py',316),
  ('names_lst -> NAME names_lst','names_lst',2,'p_names_lst','parser.py',324),
  ('names_lst -> NAME','names_lst',1,'p_names_lst','parser.py',325),
  ('type -> NAME','type',1,'p_type','parser.py',335),
  ('constant -> NAME','constant',1,'p_constant','parser.py',340),
]
