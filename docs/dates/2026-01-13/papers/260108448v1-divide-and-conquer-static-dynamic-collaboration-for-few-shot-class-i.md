---
layout: default
title: Divide and Conquer: Static-Dynamic Collaboration for Few-Shot Class-Incremental Learning
---

# Divide and Conquer: Static-Dynamic Collaboration for Few-Shot Class-Incremental Learning
**arXiv**：[2601.08448v1](https://arxiv.org/abs/2601.08448) · [PDF](https://arxiv.org/pdf/2601.08448.pdf)  
**作者**：Kexin Bao, Daichi Zhang, Yong Li, Dan Zeng, Shiming Ge  

**一句话要点**：提出静态-动态协作框架以解决少样本类增量学习中的稳定性-可塑性困境

**关键词**：少样本类增量学习, 稳定性-可塑性困境, 静态-动态协作, 静态记忆, 动态投影器, 基准测试

## 3 点简述
- 核心问题：少样本类增量学习面临稳定性-可塑性困境，需平衡旧知识保留与新知识学习。
- 方法要点：将任务分为静态保留阶段和动态学习阶段，分别利用静态记忆和动态投影器协作优化。
- 实验或效果：在三个公共基准和真实数据集上实现最先进性能，验证了方法的有效性。

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) aims to continuously recognize novel classes under limited data, which suffers from the key stability-plasticity dilemma: balancing the retention of old knowledge with the acquisition of new knowledge. To address this issue, we divide the task into two different stages and propose a framework termed Static-Dynamic Collaboration (SDC) to achieve a better trade-off between stability and plasticity. Specifically, our method divides the normal pipeline of FSCIL into Static Retaining Stage (SRS) and Dynamic Learning Stage (DLS), which harnesses old static and incremental dynamic class information, respectively. During SRS, we train an initial model with sufficient data in the base session and preserve the key part as static memory to retain fundamental old knowledge. During DLS, we introduce an extra dynamic projector jointly trained with the previous static memory. By employing both stages, our method achieves improved retention of old knowledge while continuously adapting to new classes. Extensive experiments on three public benchmarks and a real-world application dataset demonstrate that our method achieves state-of-the-art performance against other competitors.

