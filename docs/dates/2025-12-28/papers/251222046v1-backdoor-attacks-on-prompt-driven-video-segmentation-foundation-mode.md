---
layout: default
title: Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models
---

# Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models
**arXiv**：[2512.22046v1](https://arxiv.org/abs/2512.22046) · [PDF](https://arxiv.org/pdf/2512.22046.pdf)  
**作者**：Zongmin Zhang, Zhen Sun, Yifan Liao, Wenhan Dong, Xinlei He, Xingshuo Han, Shengmin Xu, Xinyi Huang  

**一句话要点**：提出BadVSFM框架以解决提示驱动视频分割基础模型的后门攻击难题

**关键词**：后门攻击, 视频分割基础模型, 提示驱动模型, 两阶段训练, 梯度冲突分析, 注意力可视化

## 3 点简述
- 核心问题：传统后门攻击对提示驱动视频分割基础模型无效，攻击成功率低于5%
- 方法要点：采用两阶段策略，先引导图像编码器，再训练掩码解码器，实现可控后门效果
- 实验或效果：在多个模型和数据集上验证，保持清洁分割质量，且现有防御方法基本无效

## 摘要（原文）

> Prompt-driven Video Segmentation Foundation Models (VSFMs) such as SAM2 are increasingly deployed in applications like autonomous driving and digital pathology, raising concerns about backdoor threats. Surprisingly, we find that directly transferring classic backdoor attacks (e.g., BadNet) to VSFMs is almost ineffective, with ASR below 5\%. To understand this, we study encoder gradients and attention maps and observe that conventional training keeps gradients for clean and triggered samples largely aligned, while attention still focuses on the true object, preventing the encoder from learning a distinct trigger-related representation. To address this challenge, we propose BadVSFM, the first backdoor framework tailored to prompt-driven VSFMs. BadVSFM uses a two-stage strategy: (1) steer the image encoder so triggered frames map to a designated target embedding while clean frames remain aligned with a clean reference encoder; (2) train the mask decoder so that, across prompt types, triggered frame-prompt pairs produce a shared target mask, while clean outputs stay close to a reference decoder. Extensive experiments on two datasets and five VSFMs show that BadVSFM achieves strong, controllable backdoor effects under diverse triggers and prompts while preserving clean segmentation quality. Ablations over losses, stages, targets, trigger settings, and poisoning rates demonstrate robustness to reasonable hyperparameter changes and confirm the necessity of the two-stage design. Finally, gradient-conflict analysis and attention visualizations show that BadVSFM separates triggered and clean representations and shifts attention to trigger regions, while four representative defenses remain largely ineffective, revealing an underexplored vulnerability in current VSFMs.

