---
layout: default
title: MCMoE: Completing Missing Modalities with Mixture of Experts for Incomplete Multimodal Action Quality Assessment
---

# MCMoE: Completing Missing Modalities with Mixture of Experts for Incomplete Multimodal Action Quality Assessment
**arXiv**：[2511.17397v1](https://arxiv.org/abs/2511.17397) · [PDF](https://arxiv.org/pdf/2511.17397.pdf)  
**作者**：Huangbiao Xu, Huanqi Wu, Xiao Ke, Junyi Wu, Rui Xu, Jinglin Xu  

**一句话要点**：提出MCMoE框架，通过专家混合完成缺失模态，解决不完整多模态动作质量评估问题。

**关键词**：多模态动作质量评估, 模态缺失完成, 专家混合模型, 自适应门控生成, 跨模态表示学习, 单阶段训练

## 3 点简述
- 核心问题：推理时模态缺失导致多模态模型失效和性能下降。
- 方法要点：自适应门控模态生成器动态融合可用信息重构缺失模态。
- 实验或效果：在三个公共AQA基准上实现完整和不完整多模态学习的最优结果。

## 摘要（原文）

> Multimodal Action Quality Assessment (AQA) has recently emerged as a promising paradigm. By leveraging complementary information across shared contextual cues, it enhances the discriminative evaluation of subtle intra-class variations in highly similar action sequences. However, partial modalities are frequently unavailable at the inference stage in reality. The absence of any modality often renders existing multimodal models inoperable. Furthermore, it triggers catastrophic performance degradation due to interruptions in cross-modal interactions. To address this issue, we propose a novel Missing Completion Framework with Mixture of Experts (MCMoE) that unifies unimodal and joint representation learning in single-stage training. Specifically, we propose an adaptive gated modality generator that dynamically fuses available information to reconstruct missing modalities. We then design modality experts to learn unimodal knowledge and dynamically mix the knowledge of all experts to extract cross-modal joint representations. With a mixture of experts, missing modalities are further refined and complemented. Finally, in the training phase, we mine the complete multimodal features and unimodal expert knowledge to guide modality generation and generation-based joint representation extraction. Extensive experiments demonstrate that our MCMoE achieves state-of-the-art results in both complete and incomplete multimodal learning on three public AQA benchmarks. Code is available at https://github.com/XuHuangbiao/MCMoE.

