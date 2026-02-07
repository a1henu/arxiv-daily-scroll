---
layout: default
title: EuroLLM-22B: Technical Report
---

# EuroLLM-22B: Technical Report
**arXiv**：[2602.05879v1](https://arxiv.org/abs/2602.05879) · [PDF](https://arxiv.org/pdf/2602.05879.pdf)  
**作者**：Miguel Moura Ramos, Duarte M. Alves, Hippolyte Gisserot-Boukhlef, João Alves, Pedro Henrique Martins, Patrick Fernandes, José Pombal, Nuno M. Guerreiro, Ricardo Rei, Nicolas Boizard, Amin Farajian, Mateusz Klimaszewski, José G. C. de Souza, Barry Haddow, François Yvon, Pierre Colombo, Alexandra Birch, André F. T. Martins  

**一句话要点**：提出EuroLLM-22B以解决欧洲语言在现有大语言模型中代表性不足的问题，支持多语言需求。

**关键词**：多语言大语言模型, 欧洲语言支持, 从头训练, 指令调优, 多语言基准测试, 开源发布

## 3 点简述
- 核心问题：欧洲语言在开放大语言模型中代表性不足，影响欧洲公民使用。
- 方法要点：从头训练模型，覆盖24种欧盟官方语言和11种额外语言，包括分词器设计和数据过滤。
- 实验或效果：在多项多语言基准测试中表现优异，推理、指令遵循和翻译能力与同类模型竞争。

## 摘要（原文）

> This report presents EuroLLM-22B, a large language model trained from scratch to support the needs of European citizens by covering all 24 official European Union languages and 11 additional languages. EuroLLM addresses the issue of European languages being underrepresented and underserved in existing open large language models. We provide a comprehensive overview of EuroLLM-22B's development, including tokenizer design, architectural specifications, data filtering, and training procedures. Across a broad set of multilingual benchmarks, EuroLLM-22B demonstrates strong performance in reasoning, instruction following, and translation, achieving results competitive with models of comparable size. To support future research, we release our base and instruction-tuned models, our multilingual web pretraining data and updated EuroBlocks instruction datasets, as well as our pre-training and evaluation codebases.

