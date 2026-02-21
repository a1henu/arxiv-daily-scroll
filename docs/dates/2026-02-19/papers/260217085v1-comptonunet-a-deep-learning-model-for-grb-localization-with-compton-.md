---
layout: default
title: ComptonUNet: A Deep Learning Model for GRB Localization with Compton Cameras under Noisy and Low-Statistic Conditions
---

# ComptonUNet: A Deep Learning Model for GRB Localization with Compton Cameras under Noisy and Low-Statistic Conditions
**arXiv**：[2602.17085v1](https://arxiv.org/abs/2602.17085) · [PDF](https://arxiv.org/pdf/2602.17085.pdf)  
**作者**：Shogo Sato, Kazuo Tanaka, Shojun Ogasawara, Kazuki Yamamoto, Kazuhiko Murasaki, Ryuichi Tanida, Jun Kataoka  

**一句话要点**：提出ComptonUNet以在低统计和高噪声条件下实现伽马射线暴的稳健定位

**关键词**：伽马射线暴定位, 康普顿相机, 深度学习, 低统计数据处理, 噪声抑制, 图像重建

## 3 点简述
- 核心问题：伽马射线暴在低光子统计和强背景噪声下检测与定位困难
- 方法要点：结合直接重建模型的统计效率与图像架构的去噪能力
- 实验或效果：在模拟低地球轨道任务场景中，定位精度显著优于现有方法

## 摘要（原文）

> Gamma-ray bursts (GRBs) are among the most energetic transient phenomena in the universe and serve as powerful probes for high-energy astrophysical processes. In particular, faint GRBs originating from a distant universe may provide unique insights into the early stages of star formation. However, detecting and localizing such weak sources remains challenging owing to low photon statistics and substantial background noise. Although recent machine learning models address individual aspects of these challenges, they often struggle to balance the trade-off between statistical robustness and noise suppression. Consequently, we propose ComptonUNet, a hybrid deep learning framework that jointly processes raw data and reconstructs images for robust GRB localization. ComptonUNet was designed to operate effectively under conditions of limited photon statistics and strong background contamination by combining the statistical efficiency of direct reconstruction models with the denoising capabilities of image-based architectures. We perform realistic simulations of GRB-like events embedded in background environments representative of low-Earth orbit missions to evaluate the performance of ComptonUNet. Our results demonstrate that ComptonUNet significantly outperforms existing approaches, achieving improved localization accuracy across a wide range of low-statistic and high-background scenarios.

