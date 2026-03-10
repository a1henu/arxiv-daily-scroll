---
layout: default
title: QualiTeacher: Quality-Conditioned Pseudo-Labeling for Real-World Image Restoration
---

# QualiTeacher: Quality-Conditioned Pseudo-Labeling for Real-World Image Restoration
**arXiv**：[2603.08030v1](https://arxiv.org/abs/2603.08030) · [PDF](https://arxiv.org/pdf/2603.08030.pdf)  
**作者**：Fengyang Xiao, Jingjia Feng, Peng Hu, Dingming Zhang, Lei Xu, Guanyi Qin, Lu Li, Chunming He, Sina Farsiu  

**一句话要点**：提出QualiTeacher框架，通过质量条件化伪标签解决真实世界图像修复中的伪标签信任悖论。

**关键词**：真实世界图像修复, 伪标签监督, 质量条件化学习, 非参考图像质量评估, Mean-Teacher框架, 监督学习范式

## 3 点简述
- 核心问题：真实世界图像修复中无条件信任低质量伪标签会导致模型学习伪影，而丢弃它们又限制数据多样性。
- 方法要点：利用非参考图像质量评估模型估计伪标签质量，条件化指导学生模型学习质量分级修复流形。
- 实验或效果：在标准基准测试中作为即插即用策略提升现有伪标签框架质量，建立从非完美监督学习的新范式。

## 摘要（原文）

> Real-world image restoration (RWIR) is a highly challenging task due to the absence of clean ground-truth images. Many recent methods resort to pseudo-label (PL) supervision, often within a Mean-Teacher (MT) framework. However, these methods face a critical paradox: unconditionally trusting the often imperfect, low-quality PLs forces the student model to learn undesirable artifacts, while discarding them severely limits data diversity and impairs model generalization. In this paper, we propose QualiTeacher, a novel framework that transforms pseudo-label quality from a noisy liability into a conditional supervisory signal. Instead of filtering, QualiTeacher explicitly conditions the student model on the quality of the PLs, estimated by an ensemble of complementary non-reference image quality assessment (NR-IQA) models spanning low-level distortion and semantic-level assessment. This strategy teaches the student network to learn a quality-graded restoration manifold, enabling it to understand what constitutes different quality levels. Consequently, it can not only avoid mimicking artifacts from low-quality labels but also extrapolate to generate results of higher quality than the teacher itself. To ensure the robustness and accuracy of this quality-driven learning, we further enhance the process with a multi-augmentation scheme to diversify the PL quality spectrum, a score-based preference optimization strategy inspired by Direct Preference Optimization (DPO) to enforce a monotonically ordered quality separation, and a cropped consistency loss to prevent adversarial over-optimization (reward hacking) of the IQA models. Experiments on standard RWIR benchmarks demonstrate that QualiTeacher can serve as a plug-and-play strategy to improve the quality of the existing pseudo-labeling framework, establishing a new paradigm for learning from imperfect supervision. Code will be released.

