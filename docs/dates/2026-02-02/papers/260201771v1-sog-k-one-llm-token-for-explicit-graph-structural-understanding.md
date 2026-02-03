---
layout: default
title: <SOG_k>: One LLM Token for Explicit Graph Structural Understanding
---

# <SOG_k>: One LLM Token for Explicit Graph Structural Understanding
**arXiv**：[2602.01771v1](https://arxiv.org/abs/2602.01771) · [PDF](https://arxiv.org/pdf/2602.01771.pdf)  
**作者**：Jingyao Wu, Bin Lu, Zijun Di, Xiaoying Gan, Meng Jin, Luoyi Fu, Xinbing Wang, Chenghu Zhou  

**一句话要点**：提出<SOG_k>特殊令牌以解决大语言模型在图结构理解中的幻觉问题。

**关键词**：图结构理解, 大语言模型, 结构令牌, 拓扑感知分词, 图问答, 性能提升

## 3 点简述
- 核心问题：大语言模型处理图结构时存在结构幻觉，现有方法如文本化或软提示存在令牌消耗大或对齐差的问题。
- 方法要点：引入<SOG_k>令牌，通过拓扑感知结构分词器将图拓扑映射为单一令牌，实现显式结构输入与信息共享。
- 实验或效果：在五个图级基准测试中性能提升9.9%至41.4%，并扩展至节点级任务，代码已开源。

## 摘要（原文）

> Large language models show great potential in unstructured data understanding, but still face significant challenges with graphs due to their structural hallucination. Existing approaches mainly either verbalize graphs into natural language, which leads to excessive token consumption and scattered attention, or transform graphs into trainable continuous embeddings (i.e., soft prompt), but exhibit severe misalignment with original text tokens. To solve this problem, we propose to incorporate one special token <SOG_k> to fully represent the Structure Of Graph within a unified token space, facilitating explicit topology input and structural information sharing. Specifically, we propose a topology-aware structural tokenizer that maps each graph topology into a highly selective single token. Afterwards, we construct a set of hybrid structure Question-Answering corpora to align new structural tokens with existing text tokens. With this approach, <SOG_k> empowers LLMs to understand, generate, and reason in a concise and accurate manner. Extensive experiments on five graph-level benchmarks demonstrate the superiority of our method, achieving a performance improvement of 9.9% to 41.4% compared to the baselines while exhibiting interpretability and consistency. Furthermore, our method provides a flexible extension to node-level tasks, enabling both global and local structural understanding. The codebase is publicly available at https://github.com/Jingyao-Wu/SOG.

