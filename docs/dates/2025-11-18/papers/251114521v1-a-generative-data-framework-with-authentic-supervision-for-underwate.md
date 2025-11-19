---
layout: default
title: A Generative Data Framework with Authentic Supervision for Underwater Image Restoration and Enhancement
---

# A Generative Data Framework with Authentic Supervision for Underwater Image Restoration and Enhancement
**arXiv**：[2511.14521v1](https://arxiv.org/abs/2511.14521) · [PDF](https://arxiv.org/pdf/2511.14521.pdf)  
**作者**：Yufeng Tian, Yifan Chen, Zhe Sun, Libang Chen, Mingyu Dou, Jijun Lu, Ye Zheng, Xuelong Li  

**一句话要点**：提出生成式数据框架，利用空中图像构建合成数据集以解决水下图像恢复与增强问题

**关键词**：水下图像恢复, 图像增强, 生成式数据框架, 非配对图像翻译, 合成数据集, 颜色失真校正

## 3 点简述
- 核心问题：水下图像恢复受限于高质量配对数据稀缺，现有基准缺乏真实监督信号
- 方法要点：基于非配对图像翻译，将空中图像转换为水下退化版本，提供精确真值标签
- 实验或效果：在6种网络架构和3个测试集上，合成数据训练模型在颜色恢复和泛化性能上表现优异

## 摘要（原文）

> Underwater image restoration and enhancement are crucial for correcting color distortion and restoring image details, thereby establishing a fundamental basis for subsequent underwater visual tasks. However, current deep learning methodologies in this area are frequently constrained by the scarcity of high-quality paired datasets. Since it is difficult to obtain pristine reference labels in underwater scenes, existing benchmarks often rely on manually selected results from enhancement algorithms, providing debatable reference images that lack globally consistent color and authentic supervision. This limits the model's capabilities in color restoration, image enhancement, and generalization. To overcome this limitation, we propose using in-air natural images as unambiguous reference targets and translating them into underwater-degraded versions, thereby constructing synthetic datasets that provide authentic supervision signals for model learning. Specifically, we establish a generative data framework based on unpaired image-to-image translation, producing a large-scale dataset that covers 6 representative underwater degradation types. The framework constructs synthetic datasets with precise ground-truth labels, which facilitate the learning of an accurate mapping from degraded underwater images to their pristine scene appearances. Extensive quantitative and qualitative experiments across 6 representative network architectures and 3 independent test sets show that models trained on our synthetic data achieve comparable or superior color restoration and generalization performance to those trained on existing benchmarks. This research provides a reliable and scalable data-driven solution for underwater image restoration and enhancement. The generated dataset is publicly available at: https://github.com/yftian2025/SynUIEDatasets.git.

