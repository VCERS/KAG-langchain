#!/usr/bin/python3

from typing import Dict, Optional
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

def spg_extract(tokenizer):
  class Output(BaseModel):
    entity: str = Field(description = '实体文本')
    category: str = Field(description = '实体类别')
    properties: Optional[Dict[str]] = Field(None, description = '实体的属性')
  parser = JsonOutputParser(pydantic_object = Output)
  instructions = parser.get_format_instructions()
  instructions = instructions.replace('{','{{')
  instructions = instructions.replace('}','}}')
  examples = [
        {
            "input": "甲状腺结节是指在甲状腺内的肿块，可随吞咽动作随甲状腺而上下移动，是临床常见的病症，可由多种病因引起。临床上有多种甲状腺疾病，如甲状腺退行性变、炎症、自身免疫以及新生物等都可以表现为结节。甲状腺结节可以单发，也可以多发，多发结节比单发结节的发病率高，但单发结节甲状腺癌的发生率较高。患者通常可以选择在普外科，甲状腺外科，内分泌科，头颈外科挂号就诊。有些患者可以触摸到自己颈部前方的结节。在大多情况下，甲状腺结节没有任何症状，甲状腺功能也是正常的。甲状腺结节进展为其它甲状腺疾病的概率只有1%。有些人会感觉到颈部疼痛、咽喉部异物感，或者存在压迫感。当甲状腺结节发生囊内自发性出血时，疼痛感会更加强烈。治疗方面，一般情况下可以用放射性碘治疗，复方碘口服液(Lugol液)等，或者服用抗甲状腺药物来抑制甲状腺激素的分泌。目前常用的抗甲状腺药物是硫脲类化合物，包括硫氧嘧啶类的丙基硫氧嘧啶(PTU)和甲基硫氧嘧啶(MTU)及咪唑类的甲硫咪唑和卡比马唑。",
            "schema": {
                "Disease": {
                    "properties": {
                        "complication": "并发症",
                        "commonSymptom": "常见症状",
                        "applicableMedicine": "适用药品",
                        "department": "就诊科室",
                        "diseaseSite": "发病部位",
                    }
                },"Medicine": {
                    "properties": {
                    }
                }
            },
            "output": [
                {
                    "entity": "甲状腺结节",
                    "category":"Disease"
                    "properties": {
                        "complication": "甲状腺癌",
                        "commonSymptom": ["颈部疼痛", "咽喉部异物感", "压迫感"],
                        "applicableMedicine": ["复方碘口服液(Lugol液)", "丙基硫氧嘧啶(PTU)", "甲基硫氧嘧啶(MTU)", "甲硫咪唑", "卡比马唑"],
                        "department": ["普外科", "甲状腺外科", "内分泌科", "头颈外科"],
                        "diseaseSite": "甲状腺",
                    }
                },{
                    "entity":"复方碘口服液(Lugol液)",
                    "category":"Medicine"
                },{
                    "entity":"丙基硫氧嘧啶(PTU)",
                    "category":"Medicine"
                },{
                    "entity":"甲基硫氧嘧啶(MTU)",
                    "category":"Medicine"
                },{
                    "entity":"甲硫咪唑",
                    "category":"Medicine"
                },{
                    "entity":"卡比马唑",
                    "category":"Medicine"
                }
            ],
        }
  ]

