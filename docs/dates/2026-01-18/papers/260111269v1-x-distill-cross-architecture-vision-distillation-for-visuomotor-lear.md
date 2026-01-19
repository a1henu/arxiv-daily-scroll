---
layout: default
title: X-Distill: Cross-Architecture Vision Distillation for Visuomotor Learning
---

# X-Distill: Cross-Architecture Vision Distillation for Visuomotor Learning
**arXiv**：[2601.11269v1](https://arxiv.org/abs/2601.11269) · [PDF](https://arxiv.org/pdf/2601.11269.pdf)  
**作者**：Maanping Shao, Feihong Zhang, Gu Zhang, Baiye Cheng, Zhengrong Xue, Huazhe Xu  

**一句话要点**：提出X-Distill方法，通过跨架构知识蒸馏解决机器人视觉运动学习中数据稀缺问题。

**关键词**：视觉运动学习, 知识蒸馏, 跨架构蒸馏, 机器人操作, 数据高效学习, 视觉表示迁移

## 3 点简述
- 核心问题：机器人学习中数据稀缺，大模型ViT泛化强但数据需求高，小模型CNN易优化但泛化弱。
- 方法要点：离线蒸馏，将DINOv2教师模型知识迁移到ResNet-18学生模型，再与扩散策略头联合微调。
- 实验或效果：在34个模拟和5个真实任务中超越从头训练ResNet、微调DINOv2及3D编码器，实现高效性能。

## 摘要（原文）

> Visuomotor policies often leverage large pre-trained Vision Transformers (ViTs) for their powerful generalization capabilities. However, their significant data requirements present a major challenge in the data-scarce context of most robotic learning settings, where compact CNNs with strong inductive biases can be more easily optimized. To address this trade-off, we introduce X-Distill, a simple yet highly effective method that synergizes the strengths of both architectures. Our approach involves an offline, cross-architecture knowledge distillation, transferring the rich visual representations of a large, frozen DINOv2 teacher to a compact ResNet-18 student on the general-purpose ImageNet dataset. This distilled encoder, now endowed with powerful visual priors, is then jointly fine-tuned with a diffusion policy head on the target manipulation tasks. Extensive experiments on $34$ simulated benchmarks and $5$ challenging real-world tasks demonstrate that our method consistently outperforms policies equipped with from-scratch ResNet or fine-tuned DINOv2 encoders. Notably, X-Distill also surpasses 3D encoders that utilize privileged point cloud observations or much larger Vision-Language Models. Our work highlights the efficacy of a simple, well-founded distillation strategy for achieving state-of-the-art performance in data-efficient robotic manipulation.

