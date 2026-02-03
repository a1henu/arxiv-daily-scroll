---
layout: default
title: Teacher-Guided Student Self-Knowledge Distillation Using Diffusion Model
---

# Teacher-Guided Student Self-Knowledge Distillation Using Diffusion Model
**arXiv**：[2602.02107v1](https://arxiv.org/abs/2602.02107) · [PDF](https://arxiv.org/pdf/2602.02107.pdf)  
**作者**：Yu Wang, Chuanguang Yang, Zhulin An, Weilun Feng, Jiarui Zhao, Chengqing Yu, Libo Huang, Boyu Diao, Yongjun Xu  

**一句话要点**：提出教师引导的学生自知识蒸馏方法DSKD，利用扩散模型解决师生特征分布差异问题。

**关键词**：知识蒸馏, 扩散模型, 特征蒸馏, 视觉识别, 自蒸馏

## 3 点简述
- 核心问题：传统知识蒸馏中师生特征分布差异导致学生学习不兼容信息。
- 方法要点：通过轻量扩散模型，用教师分类器引导去噪学生特征，并引入LSH引导的特征蒸馏。
- 实验或效果：在视觉识别任务中，DSKD显著优于现有方法，提升模型性能。

## 摘要（原文）

> Existing Knowledge Distillation (KD) methods often align feature information between teacher and student by exploring meaningful feature processing and loss functions. However, due to the difference in feature distributions between the teacher and student, the student model may learn incompatible information from the teacher. To address this problem, we propose teacher-guided student Diffusion Self-KD, dubbed as DSKD. Instead of the direct teacher-student alignment, we leverage the teacher classifier to guide the sampling process of denoising student features through a light-weight diffusion model. We then propose a novel locality-sensitive hashing (LSH)-guided feature distillation method between the original and denoised student features. The denoised student features encapsulate teacher knowledge and could be regarded as a teacher role. In this way, our DSKD method could eliminate discrepancies in mapping manners and feature distributions between the teacher and student, while learning meaningful knowledge from the teacher. Experiments on visual recognition tasks demonstrate that DSKD significantly outperforms existing KD methods across various models and datasets. Our code is attached in supplementary material.

