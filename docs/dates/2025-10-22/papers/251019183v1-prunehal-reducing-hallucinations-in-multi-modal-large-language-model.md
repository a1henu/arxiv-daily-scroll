---
layout: default
title: PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning
---

# PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning
**arXiv**：[2510.19183v1](https://arxiv.org/abs/2510.19183) · [PDF](https://arxiv.org/pdf/2510.19183.pdf)  
**作者**：Fengyuan Sun, Hui Chen, Xinhao Xu, Dandan Zheng, Jingdong Chen, Jun Zhou, Jungong Han, Guiguang Ding  

**一句话要点**：提出PruneHal方法，通过自适应KV缓存剪枝减少多模态大语言模型中的幻觉问题

**关键词**：多模态大语言模型, 幻觉缓解, KV缓存剪枝, 注意力机制, 训练无关方法

## 3 点简述
- 核心问题：多模态大语言模型幻觉与视觉令牌注意力不足相关，冗余令牌分散注意力
- 方法要点：采用训练无关的自适应KV缓存剪枝，增强对关键视觉信息的关注
- 实验或效果：在多个基准测试中验证，无需额外训练且推理成本几乎为零

## 摘要（原文）

> While multi-modal large language models (MLLMs) have made significant
> progress in recent years, the issue of hallucinations remains a major
> challenge. To mitigate this phenomenon, existing solutions either introduce
> additional data for further training or incorporate external or internal
> information during inference. However, these approaches inevitably introduce
> extra computational costs. In this paper, we observe that hallucinations in
> MLLMs are strongly associated with insufficient attention allocated to visual
> tokens. In particular, the presence of redundant visual tokens disperses the
> model's attention, preventing it from focusing on the most informative ones. As
> a result, critical visual cues are often under-attended, which in turn
> exacerbates the occurrence of hallucinations. Building on this observation, we
> propose \textbf{PruneHal}, a training-free, simple yet effective method that
> leverages adaptive KV cache pruning to enhance the model's focus on critical
> visual information, thereby mitigating hallucinations. To the best of our
> knowledge, we are the first to apply token pruning for hallucination mitigation
> in MLLMs. Notably, our method don't require additional training and incurs
> nearly no extra inference cost. Moreover, PruneHal is model-agnostic and can be
> seamlessly integrated with different decoding strategies, including those
> specifically designed for hallucination mitigation. We evaluate PruneHal on
> several widely used hallucination evaluation benchmarks using four mainstream
> MLLMs, achieving robust and outstanding results that highlight the
> effectiveness and superiority of our method. Our code will be publicly
> available.

