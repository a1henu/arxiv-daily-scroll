---
layout: default
title: InfoSculpt: Sculpting the Latent Space for Generalized Category Discovery
---

# InfoSculpt: Sculpting the Latent Space for Generalized Category Discovery
**arXiv**：[2601.10098v1](https://arxiv.org/abs/2601.10098) · [PDF](https://arxiv.org/pdf/2601.10098.pdf)  
**作者**：Wenwen Liao, Hang Ruan, Jianbo Yu, Yuansong Wang, Qingchao Jiang, Xiaofeng Yang  

**一句话要点**：提出InfoSculpt框架，基于信息瓶颈原理解决广义类别发现中的表示解耦问题。

**关键词**：广义类别发现, 信息瓶颈, 表示学习, 条件互信息, 解耦表示

## 3 点简述
- 核心问题：广义类别发现缺乏机制从实例噪声中解耦类别定义信号。
- 方法要点：通过双条件互信息目标，在标注数据上学习紧凑表示，在全数据上压缩增强噪声。
- 实验或效果：在8个基准测试中验证了信息论方法的有效性。

## 摘要（原文）

> Generalized Category Discovery (GCD) aims to classify instances from both known and novel categories within a large-scale unlabeled dataset, a critical yet challenging task for real-world, open-world applications. However, existing methods often rely on pseudo-labeling, or two-stage clustering, which lack a principled mechanism to explicitly disentangle essential, category-defining signals from instance-specific noise. In this paper, we address this fundamental limitation by re-framing GCD from an information-theoretic perspective, grounded in the Information Bottleneck (IB) principle. We introduce InfoSculpt, a novel framework that systematically sculpts the representation space by minimizing a dual Conditional Mutual Information (CMI) objective. InfoSculpt uniquely combines a Category-Level CMI on labeled data to learn compact and discriminative representations for known classes, and a complementary Instance-Level CMI on all data to distill invariant features by compressing augmentation-induced noise. These two objectives work synergistically at different scales to produce a disentangled and robust latent space where categorical information is preserved while noisy, instance-specific details are discarded. Extensive experiments on 8 benchmarks demonstrate that InfoSculpt validating the effectiveness of our information-theoretic approach.

