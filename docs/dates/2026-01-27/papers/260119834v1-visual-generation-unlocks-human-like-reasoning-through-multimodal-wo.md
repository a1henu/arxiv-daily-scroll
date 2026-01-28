---
layout: default
title: Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models
---

# Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models
**arXiv**：[2601.19834v1](https://arxiv.org/abs/2601.19834) · [PDF](https://arxiv.org/pdf/2601.19834.pdf)  
**作者**：Jialong Wu, Xiaoying Zhang, Hongyi Yuan, Xiangcheng Zhang, Tianhao Huang, Changjing He, Chaoyi Deng, Renrui Zhang, Youbin Wu, Mingsheng Long  

**一句话要点**：提出视觉生成作为世界模型以增强物理空间推理，通过视觉-语言交织推理提升多模态AI性能。

**关键词**：多模态世界模型, 视觉生成, 视觉-语言交织推理, 物理空间推理, 视觉优越性假设, VisWorld-Eval

## 3 点简述
- 核心问题：当前AI在物理空间推理中落后于人类，纯语言世界模型存在表示限制或先验知识不足的瓶颈。
- 方法要点：基于世界模型视角，提出视觉优越性假设，形式化视觉生成作为世界模型在推理中的作用。
- 实验或效果：构建VisWorld-Eval评估套件，实验显示视觉-语言交织推理在视觉世界建模任务中显著优于纯语言推理。

## 摘要（原文）

> Humans construct internal world models and reason by manipulating the concepts within these models. Recent advances in AI, particularly chain-of-thought (CoT) reasoning, approximate such human cognitive abilities, where world models are believed to be embedded within large language models. Expert-level performance in formal and abstract domains such as mathematics and programming has been achieved in current systems by relying predominantly on verbal reasoning. However, they still lag far behind humans in domains like physical and spatial intelligence, which require richer representations and prior knowledge. The emergence of unified multimodal models (UMMs) capable of both verbal and visual generation has therefore sparked interest in more human-like reasoning grounded in complementary multimodal pathways, though their benefits remain unclear. From a world-model perspective, this paper presents the first principled study of when and how visual generation benefits reasoning. Our key position is the visual superiority hypothesis: for certain tasks--particularly those grounded in the physical world--visual generation more naturally serves as world models, whereas purely verbal world models encounter bottlenecks arising from representational limitations or insufficient prior knowledge. Theoretically, we formalize internal world modeling as a core component of CoT reasoning and analyze distinctions among different forms of world models. Empirically, we identify tasks that necessitate interleaved visual-verbal CoT reasoning, constructing a new evaluation suite, VisWorld-Eval. Controlled experiments on a state-of-the-art UMM show that interleaved CoT significantly outperforms purely verbal CoT on tasks that favor visual world modeling, but offers no clear advantage otherwise. Together, this work clarifies the potential of multimodal world modeling for more powerful, human-like multimodal AI.

