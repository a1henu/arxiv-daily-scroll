---
layout: default
title: Benchmarking Real-World Medical Image Classification with Noisy Labels: Challenges, Practice, and Outlook
---

# Benchmarking Real-World Medical Image Classification with Noisy Labels: Challenges, Practice, and Outlook
**arXiv**：[2512.09315v1](https://arxiv.org/abs/2512.09315) · [PDF](https://arxiv.org/pdf/2512.09315.pdf)  
**作者**：Yuan Ma, Junlin Hou, Chao Zhang, Yukun Zhou, Zongyuan Ge, Haoran Xie, Lie Ju  

**一句话要点**：提出LNMBench基准以评估医学图像分类中带噪标签方法的鲁棒性

**关键词**：医学图像分类, 带噪标签学习, 基准评估, 鲁棒性分析, 多模态数据

## 3 点简述
- 核心问题：医学图像标注噪声高且现有方法鲁棒性未系统评估
- 方法要点：构建统一基准，涵盖10种方法、7数据集、6模态和3噪声模式
- 实验或效果：现有方法在高噪声下性能显著下降，提出改进增强鲁棒性

## 摘要（原文）

> Learning from noisy labels remains a major challenge in medical image analysis, where annotation demands expert knowledge and substantial inter-observer variability often leads to inconsistent or erroneous labels. Despite extensive research on learning with noisy labels (LNL), the robustness of existing methods in medical imaging has not been systematically assessed. To address this gap, we introduce LNMBench, a comprehensive benchmark for Label Noise in Medical imaging. LNMBench encompasses \textbf{10} representative methods evaluated across 7 datasets, 6 imaging modalities, and 3 noise patterns, establishing a unified and reproducible framework for robustness evaluation under realistic conditions. Comprehensive experiments reveal that the performance of existing LNL methods degrades substantially under high and real-world noise, highlighting the persistent challenges of class imbalance and domain variability in medical data. Motivated by these findings, we further propose a simple yet effective improvement to enhance model robustness under such conditions. The LNMBench codebase is publicly released to facilitate standardized evaluation, promote reproducible research, and provide practical insights for developing noise-resilient algorithms in both research and real-world medical applications.The codebase is publicly available on https://github.com/myyy777/LNMBench.

