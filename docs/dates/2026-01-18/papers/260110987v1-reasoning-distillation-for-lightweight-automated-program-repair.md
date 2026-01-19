---
layout: default
title: Reasoning Distillation for Lightweight Automated Program Repair
---

# Reasoning Distillation for Lightweight Automated Program Repair
**arXiv**：[2601.10987v1](https://arxiv.org/abs/2601.10987) · [PDF](https://arxiv.org/pdf/2601.10987.pdf)  
**作者**：Aanand Balasubramanian, Sashank Silwal  

**一句话要点**：提出推理蒸馏方法以提升轻量级自动程序修复模型的修复类型分类性能

**关键词**：自动程序修复, 推理蒸馏, 轻量级模型, 符号推理, 修复类型分类, CodeT5

## 3 点简述
- 研究轻量级符号推理监督能否改善紧凑模型在资源受限环境下的修复分类
- 方法使用大型教师模型提供结构化符号推理标签，训练基于CodeT5的学生模型
- 实验显示推理监督提升宏观平均性能，尤其在低频错误类别，不增加模型复杂度

## 摘要（原文）

> We study whether lightweight symbolic reasoning supervision can improve fix type classification in compact automated program repair models. Small code models are attractive for resource-constrained settings, but they typically produce only a single prediction, making it unclear whether they learn meaningful program structure or rely on shallow correlations. We propose a reasoning distillation approach in which a large teacher model provides structured symbolic reasoning tags alongside fix-type labels. These tags capture high-level causal properties of bugs without relying on free-form explanations. We train a CodeT5-based student model under label-only and reasoning-distilled settings on the IntroClass benchmark. Reasoning supervision consistently improves macro averaged performance, particularly on less frequent bug categories, without increasing model size or complexity. We further analyze the relationship between reasoning accuracy and fix-type prediction, showing that correct reasoning traces strongly correlate with correct predictions, while not fully determining them. Our results suggest that symbolic reasoning distillation is a practical way to improve interpretability and robustness in lightweight program repair models.

