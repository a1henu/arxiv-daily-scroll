---
layout: default
title: Data-Centric Visual Development for Self-Driving Labs
---

# Data-Centric Visual Development for Self-Driving Labs
**arXiv**：[2512.02018v1](https://arxiv.org/abs/2512.02018) · [PDF](https://arxiv.org/pdf/2512.02018.pdf)  
**作者**：Anbang Liu, Guanzhong Hu, Jiayi Wang, Ping Guo, Han Liu  

**一句话要点**：提出混合真实与虚拟数据生成方法，以解决自驱动实验室中移液气泡检测的数据稀缺问题。

**关键词**：自驱动实验室, 移液检测, 数据增强, 混合数据生成, 气泡检测, 视觉反馈

## 3 点简述
- 核心问题：自驱动实验室中移液操作精度要求高，但训练数据稀缺，尤其是负样本难以获取。
- 方法要点：构建混合管道，结合人机协同的真实数据采集与基于参考条件的虚拟图像生成，以增强数据集。
- 实验或效果：在真实测试集上，仅用真实数据训练的模型准确率达99.6%，混合数据训练维持99.4%准确率，降低数据收集负担。

## 摘要（原文）

> Self-driving laboratories offer a promising path toward reducing the labor-intensive, time-consuming, and often irreproducible workflows in the biological sciences. Yet their stringent precision requirements demand highly robust models whose training relies on large amounts of annotated data. However, this kind of data is difficult to obtain in routine practice, especially negative samples. In this work, we focus on pipetting, the most critical and precision sensitive action in SDLs. To overcome the scarcity of training data, we build a hybrid pipeline that fuses real and virtual data generation. The real track adopts a human-in-the-loop scheme that couples automated acquisition with selective human verification to maximize accuracy with minimal effort. The virtual track augments the real data using reference-conditioned, prompt-guided image generation, which is further screened and validated for reliability. Together, these two tracks yield a class-balanced dataset that enables robust bubble detection training. On a held-out real test set, a model trained entirely on automatically acquired real images reaches 99.6% accuracy, and mixing real and generated data during training sustains 99.4% accuracy while reducing collection and review load. Our approach offers a scalable and cost-effective strategy for supplying visual feedback data to SDL workflows and provides a practical solution to data scarcity in rare event detection and broader vision tasks.

