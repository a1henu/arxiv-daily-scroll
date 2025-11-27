---
layout: default
title: Generalized Design Choices for Deepfake Detectors
---

# Generalized Design Choices for Deepfake Detectors
**arXiv**：[2511.21507v1](https://arxiv.org/abs/2511.21507) · [PDF](https://arxiv.org/pdf/2511.21507.pdf)  
**作者**：Lorenzo Pellegrini, Serafino Pandolfini, Davide Maltoni, Matteo Ferrara, Marco Prati, Marco Ramilli  

**一句话要点**：系统研究深度伪造检测器的设计选择以提升准确性和泛化能力

**关键词**：深度伪造检测, 设计选择分析, 模型泛化, AI-GenBench基准, 实现细节影响

## 3 点简述
- 核心问题：深度伪造检测器性能常依赖实现细节，难以公平比较和识别关键因素。
- 方法要点：通过隔离个体因素，研究训练、推理和增量更新对检测模型的影响。
- 实验或效果：在AI-GenBench基准上实现先进性能，识别一致改进的设计选择。

## 摘要（原文）

> The effectiveness of deepfake detection methods often depends less on their core design and more on implementation details such as data preprocessing, augmentation strategies, and optimization techniques. These factors make it difficult to fairly compare detectors and to understand which factors truly contribute to their performance. To address this, we systematically investigate how different design choices influence the accuracy and generalization capabilities of deepfake detection models, focusing on aspects related to training, inference, and incremental updates. By isolating the impact of individual factors, we aim to establish robust, architecture-agnostic best practices for the design and development of future deepfake detection systems. Our experiments identify a set of design choices that consistently improve deepfake detection and enable state-of-the-art performance on the AI-GenBench benchmark.

