---
layout: default
title: Density-Guided Response Optimization: Community-Grounded Alignment via Implicit Acceptance Signals
---

# Density-Guided Response Optimization: Community-Grounded Alignment via Implicit Acceptance Signals
**arXiv**：[2603.03242v1](https://arxiv.org/abs/2603.03242) · [PDF](https://arxiv.org/pdf/2603.03242.pdf)  
**作者**：Patrick Gerard, Svitlana Volkova  

**一句话要点**：提出密度引导响应优化方法，利用隐式接受信号对齐语言模型至社区规范

**关键词**：语言模型对齐, 隐式偏好学习, 社区规范适应, 密度引导优化, 表示空间几何

## 3 点简述
- 问题：在线社区规范多样，显式偏好监督成本高或伦理风险大，难以对齐语言模型
- 方法：基于接受行为在表示空间形成高密度区域，设计密度引导优化，无需显式标签
- 效果：在标注稀缺社区中，优化模型响应优于监督和提示基线，获人类和模型偏好

## 摘要（原文）

> Language models deployed in online communities must adapt to norms that vary across social, cultural, and domain-specific contexts. Prior alignment approaches rely on explicit preference supervision or predefined principles, which are effective for well-resourced settings but exclude most online communities -- particularly those without institutional backing, annotation infrastructure, or organized around sensitive topics -- where preference elicitation is costly, ethically fraught, or culturally misaligned.
>   We observe that communities already express preferences implicitly through what content they accept, engage with, and allow to persist. We show that this acceptance behavior induces measurable geometric structure in representation space: accepted responses occupy coherent, high-density regions that reflect community-specific norms, while rejected content falls in sparser or misaligned areas. We operationalize this structure as an implicit preference signal for alignment and introduce density-guided response optimization (DGRO), a method that aligns language models to community norms without requiring explicit preference labels.
>   Using labeled preference data, we demonstrate that local density recovers pairwise community judgments, indicating that geometric structure encodes meaningful preference signal. We then apply DGRO in annotation-scarce settings across diverse communities spanning platform, topic, and language. DGRO-aligned models consistently produce responses preferred by human annotators, domain experts, and model-based judges over supervised and prompt-based baselines. We position DGRO as a practical alignment alternative for communities where explicit preference supervision is unavailable or misaligned with situated practices, and discuss the implications and risks of learning from emergent acceptance behavior.

