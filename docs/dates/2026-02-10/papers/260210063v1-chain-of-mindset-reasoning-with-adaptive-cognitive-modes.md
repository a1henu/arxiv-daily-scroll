---
layout: default
title: Chain of Mindset: Reasoning with Adaptive Cognitive Modes
---

# Chain of Mindset: Reasoning with Adaptive Cognitive Modes
**arXiv**：[2602.10063v1](https://arxiv.org/abs/2602.10063) · [PDF](https://arxiv.org/pdf/2602.10063.pdf)  
**作者**：Tianyi Jiang, Arctanx An, Hengyi Feng, Naixin Zhai, Haodong Li, Xiaomin Yu, Jiahui Liu, Hanwen Du, Shuo Zhang, Zhi Yang, Jie Huang, Yuhua Li, Yongxin Ni, Huacan Wang, Ronghao Chen  

**一句话要点**：提出Chain of Mindset框架，通过自适应认知模式提升大语言模型推理能力

**关键词**：认知模式推理, 自适应框架, 大语言模型, 思维链, 多模态基准, 训练无关方法

## 3 点简述
- 现有LLM推理方法固定单一认知模式，忽视问题解决不同阶段需不同思维方式
- CoM框架分解推理为四种异构认知模式，由元代理动态选择，上下文门过滤信息流
- 在数学、代码生成等六个基准测试中，CoM实现SOTA性能，准确率提升约4.7-5.0%

## 摘要（原文）

> Human problem-solving is never the repetition of a single mindset, by which we mean a distinct mode of cognitive processing. When tackling a specific task, we do not rely on a single mindset; instead, we integrate multiple mindsets within the single solution process. However, existing LLM reasoning methods fall into a common trap: they apply the same fixed mindset across all steps, overlooking that different stages of solving the same problem require fundamentally different mindsets. This single-minded assumption prevents models from reaching the next level of intelligence. To address this limitation, we propose Chain of Mindset (CoM), a training-free agentic framework that enables step-level adaptive mindset orchestration. CoM decomposes reasoning into four functionally heterogeneous mindsets: Spatial, Convergent, Divergent, and Algorithmic. A Meta-Agent dynamically selects the optimal mindset based on the evolving reasoning state, while a bidirectional Context Gate filters cross-module information flow to maintain effectiveness and efficiency. Experiments across six challenging benchmarks spanning mathematics, code generation, scientific QA, and spatial reasoning demonstrate that CoM achieves state-of-the-art performance, outperforming the strongest baseline by 4.96\% and 4.72\% in overall accuracy on Qwen3-VL-32B-Instruct and Gemini-2.0-Flash, while balancing reasoning efficiency. Our code is publicly available at \href{https://github.com/QuantaAlpha/chain-of-mindset}{https://github.com/QuantaAlpha/chain-of-mindset}.

