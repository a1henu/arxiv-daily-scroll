---
layout: default
title: REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding
---

# REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding
**arXiv**：[2511.13026v1](https://arxiv.org/abs/2511.13026) · [PDF](https://arxiv.org/pdf/2511.13026.pdf)  
**作者**：Jiaze Li, Hao Yin, Wenhui Tan, Jingyang Chen, Boshen Xu, Yuxun Qu, Yijing Chen, Jianzhong Ju, Zhenbo Luo, Jian Luan  

**一句话要点**：提出REVISOR框架以增强多模态大模型在长视频理解中的反思推理能力

**关键词**：长视频理解, 多模态反思, 强化学习, 因果对齐, 工具增强推理

## 3 点简述
- 核心问题：纯文本反思机制在长视频理解中因视觉信息丰富和缺乏跨模态交互而受限
- 方法要点：引入多模态反思过程，结合DADR奖励机制强化视频证据与推理的因果对齐
- 实验或效果：在多个基准测试中显著提升性能，无需额外监督微调或外部模型

## 摘要（原文）

> Self-reflection mechanisms that rely on purely text-based rethinking processes perform well in most multimodal tasks. However, when directly applied to long-form video understanding scenarios, they exhibit clear limitations. The fundamental reasons for this lie in two points: (1)long-form video understanding involves richer and more dynamic visual input, meaning rethinking only the text information is insufficient and necessitates a further rethinking process specifically targeting visual information; (2) purely text-based reflection mechanisms lack cross-modal interaction capabilities, preventing them from fully integrating visual information during reflection. Motivated by these insights, we propose REVISOR (REflective VIsual Segment Oriented Reasoning), a novel framework for tool-augmented multimodal reflection. REVISOR enables MLLMs to collaboratively construct introspective reflection processes across textual and visual modalities, significantly enhancing their reasoning capability for long-form video understanding. To ensure that REVISOR can learn to accurately review video segments highly relevant to the question during reinforcement learning, we designed the Dual Attribution Decoupled Reward (DADR) mechanism. Integrated into the GRPO training strategy, this mechanism enforces causal alignment between the model's reasoning and the selected video evidence. Notably, the REVISOR framework significantly enhances long-form video understanding capability of MLLMs without requiring supplementary supervised fine-tuning or external models, achieving impressive results on four benchmarks including VideoMME, LongVideoBench, MLVU, and LVBench.

