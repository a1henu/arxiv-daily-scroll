---
layout: default
title: When One Moment Isn't Enough: Multi-Moment Retrieval with Cross-Moment Interactions
---

# When One Moment Isn't Enough: Multi-Moment Retrieval with Cross-Moment Interactions
**arXiv**：[2510.17218v1](https://arxiv.org/abs/2510.17218) · [PDF](https://arxiv.org/pdf/2510.17218.pdf)  
**作者**：Zhuo Cao, Heming Du, Bingqing Zhang, Xin Yu, Xue Li, Sen Wang  

**一句话要点**：提出FlashMMR框架与QV-M²数据集以解决视频多时刻检索问题

**关键词**：多时刻检索, 视频时序定位, 数据集构建, 后验证模块, 基准评估

## 3 点简述
- 核心问题：现有单时刻检索方法无法处理查询对应多个相关时刻的现实场景
- 方法要点：引入多时刻后验证模块，通过约束时间调整和验证优化时刻边界
- 实验或效果：在QV-M²数据集上，FlashMMR在多个指标上优于现有方法，提升达3.00%

## 摘要（原文）

> Existing Moment retrieval (MR) methods focus on Single-Moment Retrieval
> (SMR). However, one query can correspond to multiple relevant moments in
> real-world applications. This makes the existing datasets and methods
> insufficient for video temporal grounding. By revisiting the gap between
> current MR tasks and real-world applications, we introduce a high-quality
> datasets called QVHighlights Multi-Moment Dataset (QV-M$^2$), along with new
> evaluation metrics tailored for multi-moment retrieval (MMR). QV-M$^2$ consists
> of 2,212 annotations covering 6,384 video segments. Building on existing
> efforts in MMR, we propose a framework called FlashMMR. Specifically, we
> propose a Multi-moment Post-verification module to refine the moment
> boundaries. We introduce constrained temporal adjustment and subsequently
> leverage a verification module to re-evaluate the candidate segments. Through
> this sophisticated filtering pipeline, low-confidence proposals are pruned, and
> robust multi-moment alignment is achieved. We retrain and evaluate 6 existing
> MR methods on QV-M$^2$ and QVHighlights under both SMR and MMR settings.
> Results show that QV-M$^2$ serves as an effective benchmark for training and
> evaluating MMR models, while FlashMMR provides a strong baseline. Specifically,
> on QV-M$^2$, it achieves improvements over prior SOTA method by 3.00% on G-mAP,
> 2.70% on mAP@3+tgt, and 2.56% on mR@3. The proposed benchmark and method
> establish a foundation for advancing research in more realistic and challenging
> video temporal grounding scenarios. Code is released at
> https://github.com/Zhuo-Cao/QV-M2.

