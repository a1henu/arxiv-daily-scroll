---
layout: default
title: Orthogonium : A Unified, Efficient Library of Orthogonal and 1-Lipschitz Building Blocks
---

# Orthogonium : A Unified, Efficient Library of Orthogonal and 1-Lipschitz Building Blocks
**arXiv**：[2601.13776v1](https://arxiv.org/abs/2601.13776) · [PDF](https://arxiv.org/pdf/2601.13776.pdf)  
**作者**：Thibaut Boissin, Franck Mamalet, Valentin Lafargue, Mathieu Serrurier  

**一句话要点**：提出Orthogonium库以统一高效实现正交和1-Lipschitz神经网络层，降低鲁棒深度学习应用门槛。

**关键词**：正交神经网络, 1-Lipschitz约束, 鲁棒深度学习, PyTorch库, 对抗鲁棒性, 生成模型

## 3 点简述
- 现有正交和1-Lipschitz层实现分散、有限且计算成本高，阻碍鲁棒深度学习架构发展。
- Orthogonium提供统一PyTorch库，支持标准卷积特征并保持严格数学保证，优化实现减少大规模基准测试开销。
- 库内严格测试发现现有实现关键错误，强调标准化可靠工具重要性，促进可扩展实验和集成。

## 摘要（原文）

> Orthogonal and 1-Lipschitz neural network layers are essential building blocks in robust deep learning architectures, crucial for certified adversarial robustness, stable generative models, and reliable recurrent networks. Despite significant advancements, existing implementations remain fragmented, limited, and computationally demanding. To address these issues, we introduce Orthogonium , a unified, efficient, and comprehensive PyTorch library providing orthogonal and 1-Lipschitz layers. Orthogonium provides access to standard convolution features-including support for strides, dilation, grouping, and transposed-while maintaining strict mathematical guarantees. Its optimized implementations reduce overhead on large scale benchmarks such as ImageNet. Moreover, rigorous testing within the library has uncovered critical errors in existing implementations, emphasizing the importance of standardized and reliable tools. Orthogonium thus significantly lowers adoption barriers, enabling scalable experimentation and integration across diverse applications requiring orthogonality and robust Lipschitz constraints. Orthogonium is available at https://github.com/deel-ai/orthogonium.

