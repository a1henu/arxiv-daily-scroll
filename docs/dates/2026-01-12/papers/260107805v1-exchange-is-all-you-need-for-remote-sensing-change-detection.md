---
layout: default
title: Exchange Is All You Need for Remote Sensing Change Detection
---

# Exchange Is All You Need for Remote Sensing Change Detection
**arXiv**：[2601.07805v1](https://arxiv.org/abs/2601.07805) · [PDF](https://arxiv.org/pdf/2601.07805.pdf)  
**作者**：Sijun Dong, Siming Fu, Kaiyu Li, Xiangyong Cao, Xiaoliang Meng, Bo Du  

**一句话要点**：提出SEED范式，通过特征交换简化遥感变化检测，无需显式差异计算。

**关键词**：遥感变化检测, 特征交换, Siamese网络, 参数免费融合, SEED范式, SEG2CD

## 3 点简述
- 核心问题：遥感变化检测依赖双时相特征的有效融合与区分，现有方法常使用显式差异模块如减法或拼接。
- 方法要点：SEED采用参数免费的特征交换替代显式差异，通过共享权重实现单参数集模型，理论证明其保持互信息和贝叶斯最优风险。
- 实验或效果：在五个基准数据集和三种骨干网络上验证，SEED性能匹配或超越先进方法，并可通过SEG2CD将语义分割模型转化为变化检测器。

## 摘要（原文）

> Remote sensing change detection fundamentally relies on the effective fusion and discrimination of bi-temporal features. Prevailing paradigms typically utilize Siamese encoders bridged by explicit difference computation modules, such as subtraction or concatenation, to identify changes. In this work, we challenge this complexity with SEED (Siamese Encoder-Exchange-Decoder), a streamlined paradigm that replaces explicit differencing with parameter-free feature exchange. By sharing weights across both Siamese encoders and decoders, SEED effectively operates as a single parameter set model. Theoretically, we formalize feature exchange as an orthogonal permutation operator and prove that, under pixel consistency, this mechanism preserves mutual information and Bayes optimal risk, whereas common arithmetic fusion methods often introduce information loss. Extensive experiments across five benchmarks, including SYSU-CD, LEVIR-CD, PX-CLCD, WaterCD, and CDD, and three backbones, namely SwinT, EfficientNet, and ResNet, demonstrate that SEED matches or surpasses state of the art methods despite its simplicity. Furthermore, we reveal that standard semantic segmentation models can be transformed into competitive change detectors solely by inserting this exchange mechanism, referred to as SEG2CD. The proposed paradigm offers a robust, unified, and interpretable framework for change detection, demonstrating that simple feature exchange is sufficient for high performance information fusion. Code and full training and evaluation protocols will be released at https://github.com/dyzy41/open-rscd.

