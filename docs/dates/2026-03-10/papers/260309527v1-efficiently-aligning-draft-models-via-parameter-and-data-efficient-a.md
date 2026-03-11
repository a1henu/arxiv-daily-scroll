---
layout: default
title: Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation
---

# Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation
**arXiv**：[2603.09527v1](https://arxiv.org/abs/2603.09527) · [PDF](https://arxiv.org/pdf/2603.09527.pdf)  
**作者**：Luxi Lin, Zhihang Lin, Zhanpeng Zeng, Yuhao Chen, Qingyu Zhang, Jixiang Luo, Xuelong Li, Rongrong Ji  

**一句话要点**：提出EDA框架以高效对齐草稿模型与微调目标模型，提升推测解码性能

**关键词**：推测解码, 参数高效适应, 数据再生, 模型对齐, 大语言模型推理

## 3 点简述
- 核心问题：推测解码在目标模型微调后性能下降，重训练草稿模型成本高
- 方法要点：采用解耦架构、数据再生策略和样本选择机制，实现参数与数据高效适应
- 实验或效果：EDA恢复推测性能，提高平均接受长度，显著降低训练成本

## 摘要（原文）

> Speculative decoding accelerates LLM inference but suffers from performance degradation when target models are fine-tuned for specific domains. A naive solution is to retrain draft models for every target model, which is costly and inefficient. To address this, we introduce a parameter- and data-efficient framework named Efficient Draft Adaptation, abbreviated as EDA, for efficiently adapting draft models. EDA introduces three innovations: (1) a decoupled architecture that utilizes shared and private components to model the shared and target-specific output distributions separately, enabling parameter-efficient adaptation by updating only the lightweight private component;(2) a data regeneration strategy that utilizes the fine-tuned target model to regenerate training data, thereby improving the alignment between training and speculative decoding, leading to higher average acceptance length;(3) a sample selection mechanism that prioritizes high-value data for efficient adaptation. Our experiments show that EDA effectively restores speculative performance on fine-tuned models, achieving superior average acceptance lengths with significantly reduced training costs compared to full retraining. Code is available at https://github.com/Lyn-Lucy/Efficient-Draft-Adaptation.

