---
layout: default
title: FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models
---

# FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models
**arXiv**：[2510.11190v1](https://arxiv.org/abs/2510.11190) · [PDF](https://arxiv.org/pdf/2510.11190.pdf)  
**作者**：Shengming Yuan, Xinyu Lyu, Shuailong Wang, Beitao Chen, Jingkuan Song, Lianli Gao  

**一句话要点**：提出FlexAC框架以灵活控制多模态大语言模型中的联想推理强度

**关键词**：多模态大语言模型, 联想推理控制, 幻觉利用, 中间层调制, 训练无关框架, 创造性任务适应

## 3 点简述
- 多模态大语言模型在忠实性与创造性间存在固有权衡，现有方法缺乏灵活调节联想推理强度的能力。
- FlexAC通过修改中间层表示和利用幻觉引导向量，实现无需训练的联想推理强度调制。
- 实验显示在Creation-MMBench上创造力提升5.8倍，CHAIR上幻觉率降低29%，优于基线方法。

## 摘要（原文）

> Multimodal large language models (MLLMs) face an inherent trade-off between
> faithfulness and creativity, as different tasks require varying degrees of
> associative reasoning. However, existing methods lack the flexibility to
> modulate this reasoning strength, limiting MLLMs' adaptability across factual
> and creative scenarios. To bridge this gap, we propose equipping MLLMs with
> mechanisms that enable flexible control over associative reasoning. We begin by
> investigating the internal mechanisms underlying associative behavior in MLLMs
> and find that: (1) middle layers play a pivotal role in shaping model's
> associative tendencies, (2) modifying representations in these layers
> effectively regulates associative reasoning strength, and (3) hallucinations
> can be exploited to derive steering vectors that guide this modulation.
> Building on these findings, we introduce Flexible Association Control (FlexAC),
> a lightweight and training-free framework for modulating associative behavior
> in MLLMs. FlexAC first induces hallucination-guided intermediate
> representations to encode associative directions. Then, it selects
> high-association instances to construct effective associative steering vectors,
> whose strengths are adaptively calibrated to balance creative guidance with
> output stability. Finally, recognizing the multi-dimensional nature of
> associative reasoning, FlexAC incorporates task-specific associative vectors
> derived from a forward pass on a few target-domain samples, enabling models to
> follow diverse associative directions and better adapt to creative tasks.
> Notably, our method achieves up to a 5.8x improvement in creativity on
> Creation-MMBench and a 29% reduction in hallucination rate on CHAIR, surpassing
> existing baselines and demonstrating its effectiveness in enabling flexible
> control over associative reasoning in MLLMs. Our code is available at
> https://github.com/ylhz/FlexAC.

