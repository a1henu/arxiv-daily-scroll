---
layout: default
title: Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions
---

# Beyond Next-Token Alignment: Distilling Multimodal Large Language Models via Token Interactions
**arXiv**：[2602.09483v1](https://arxiv.org/abs/2602.09483) · [PDF](https://arxiv.org/pdf/2602.09483.pdf)  
**作者**：Lin Chen, Xiaoke Zhao, Kun Ding, Weiwei Feng, Changtao Miao, Zili Wang, Wenxuan Guo, Ying Wang, Kaiyuan Zheng, Bo Zhang, Zhe Li, Shiming Xiang  

**一句话要点**：提出Align-TI蒸馏框架，通过令牌交互对齐解决多模态大语言模型压缩问题

**关键词**：多模态大语言模型, 知识蒸馏, 令牌交互, 模型压缩, 视觉-语言对齐, 生成逻辑对齐

## 3 点简述
- 核心问题：现有知识蒸馏方法依赖静态下一令牌对齐，忽略动态令牌交互，影响多模态理解与生成能力压缩
- 方法要点：引入IVA对齐视觉-指令令牌交互以提取关键视觉信息，TPA对齐响应内令牌交互以捕捉生成逻辑
- 实验或效果：在实验中相对Vanilla KD提升2.6%，蒸馏模型Align-TI-2B超越LLaVA-1.5-7B达7.0%，实现高效参数训练

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) demonstrate impressive cross-modal capabilities, yet their substantial size poses significant deployment challenges. Knowledge distillation (KD) is a promising solution for compressing these models, but existing methods primarily rely on static next-token alignment, neglecting the dynamic token interactions, which embed essential capabilities for multimodal understanding and generation. To this end, we introduce Align-TI, a novel KD framework designed from the perspective of Token Interactions. Our approach is motivated by the insight that MLLMs rely on two primary interactions: vision-instruction token interactions to extract relevant visual information, and intra-response token interactions for coherent generation. Accordingly, Align-TI introduces two components: IVA enables the student model to imitate the teacher's instruction-relevant visual information extract capability by aligning on salient visual regions. TPA captures the teacher's dynamic generative logic by aligning the sequential token-to-token transition probabilities. Extensive experiments demonstrate Align-TI's superiority. Notably, our approach achieves $2.6\%$ relative improvement over Vanilla KD, and our distilled Align-TI-2B even outperforms LLaVA-1.5-7B (a much larger MLLM) by $7.0\%$, establishing a new state-of-the-art distillation framework for training parameter-efficient MLLMs. Code is available at https://github.com/lchen1019/Align-TI.

