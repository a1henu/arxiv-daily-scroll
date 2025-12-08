---
layout: default
title: Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs
---

# Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs
**arXiv**：[2512.05648v1](https://arxiv.org/abs/2512.05648) · [PDF](https://arxiv.org/pdf/2512.05648.pdf)  
**作者**：Igor Shilov, Alex Cloud, Aryo Pradipta Gema, Jacob Goldman-Wetzler, Nina Panickssery, Henry Sleight, Erik Jones, Cem Anil  

**一句话要点**：提出选择性梯度掩码以增强大语言模型在标签噪声下的能力移除鲁棒性

**关键词**：能力移除, 梯度路由, 标签噪声鲁棒性, 预训练安全, 参数定位, 对抗微调

## 3 点简述
- 核心问题：数据过滤在预训练时面临标签噪声挑战，可能导致危险能力残留
- 方法要点：通过选择性梯度掩码将目标知识定位到专用参数，实现更精确的移除
- 实验或效果：在双语和生物学知识移除任务中，相比基线方法提供更好的保留/遗忘权衡

## 摘要（原文）

> Large Language Models increasingly possess capabilities that carry dual-use risks. While data filtering has emerged as a pretraining-time mitigation, it faces significant challenges: labeling whether data is harmful is expensive at scale, and given improving sample efficiency with larger models, even small amounts of mislabeled content could give rise to dangerous capabilities. To address risks associated with mislabeled harmful content, prior work proposed Gradient Routing (Cloud et al., 2024) -- a technique that localizes target knowledge into a dedicated subset of model parameters so they can later be removed. We explore an improved variant of Gradient Routing, which we call Selective GradienT Masking (SGTM), with particular focus on evaluating its robustness to label noise. SGTM zero-masks selected gradients such that target domain examples only update their dedicated parameters. We test SGTM's effectiveness in two applications: removing knowledge of one language from a model trained on a bilingual synthetic dataset, and removing biology knowledge from a model trained on English Wikipedia. In both cases SGTM provides better retain/forget trade-off in the presence of labeling errors compared to both data filtering and a previously proposed instantiation of Gradient Routing. Unlike shallow unlearning approaches that can be quickly undone through fine-tuning, SGTM exhibits strong robustness to adversarial fine-tuning, requiring seven times more fine-tuning steps to reach baseline performance on the forget set compared to a finetuning-based unlearning method (RMU). Our results suggest SGTM provides a promising pretraining-time complement to existing safety mitigations, particularly in settings where label noise is unavoidable.

