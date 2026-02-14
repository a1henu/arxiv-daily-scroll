---
layout: default
title: Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging
---

# Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging
**arXiv**：[2602.11717v1](https://arxiv.org/abs/2602.11717) · [PDF](https://arxiv.org/pdf/2602.11717.pdf)  
**作者**：Weihong Lin, Lin Sun, Qilong Shi, Aomufei Yuan, Yuxuan Tian, Zhengyang Wang, Guangxiang Zhao, Xiangzheng Zhang, Tong Yang  

**一句话要点**：提出SCF-RKL稀疏互补融合框架，以解决模型合并中的功能干扰问题

**关键词**：模型合并, 稀疏融合, 反向KL散度, 分布感知更新, 功能干扰控制, 生成稳定性

## 3 点简述
- 现有模型合并方法依赖参数空间启发式，导致严重干扰和性能下降
- SCF-RKL使用反向KL散度衡量功能差异，通过稀疏、分布感知更新选择性融合互补参数
- 在24个基准测试中，SCF-RKL优于现有方法，保持强泛化和生成稳定性

## 摘要（原文）

> Model merging has emerged as a promising paradigm for composing the capabilities of large language models by directly operating in weight space, enabling the integration of specialized models without costly retraining. However, existing merging methods largely rely on parameter-space heuristics, which often introduce severe interference, leading to degraded generalization and unstable generation behaviors such as repetition and incoherent outputs. In this work, we propose Sparse Complementary Fusion with reverse KL (SCF-RKL), a novel model merging framework that explicitly controls functional interference through sparse, distribution-aware updates. Instead of assuming linear additivity in parameter space, SCF-RKL measures the functional divergence between models using reverse Kullback-Leibler divergence and selectively incorporates complementary parameters. This mode-seeking, sparsity-inducing design effectively preserves stable representations while integrating new capabilities. We evaluate SCF-RKL across a wide range of model scales and architectures, covering both reasoning-focused and instruction-tuned models. Extensive experiments on 24 benchmarks spanning advanced reasoning, general reasoning and knowledge, instruction following, and safety demonstrate, vision classification that SCF-RKL consistently outperforms existing model merging methods while maintaining strong generalization and generation stability.

