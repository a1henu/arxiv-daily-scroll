---
layout: default
title: ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification
---

# ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification
**arXiv**：[2601.03600v1](https://arxiv.org/abs/2601.03600) · [PDF](https://arxiv.org/pdf/2601.03600.pdf)  
**作者**：Xiao Lin, Philip Li, Zhichen Zeng, Tingwei Li, Tianxin Wei, Xuying Ning, Gaotang Li, Yuzhong Chen, Hanghang Tong  

**一句话要点**：提出ALERT框架以解决零样本大语言模型越狱检测问题

**关键词**：零样本检测, 大语言模型安全, 越狱攻击, 特征放大, 内部差异分析, 安全基准测试

## 3 点简述
- 核心问题：现有检测方法依赖训练数据中的越狱模板，难以应对零样本场景下新攻击的挑战。
- 方法要点：通过层级、模块和词元级放大内部特征差异，识别安全相关层、模块和词元，构建高效检测器。
- 实验或效果：在三个安全基准测试中，ALERT在零样本检测性能上表现优异，常居前二，平均准确率和F1分数显著提升。

## 摘要（原文）

> Despite rich safety alignment strategies, large language models (LLMs) remain highly susceptible to jailbreak attacks, which compromise safety guardrails and pose serious security risks. Existing detection methods mainly detect jailbreak status relying on jailbreak templates present in the training data. However, few studies address the more realistic and challenging zero-shot jailbreak detection setting, where no jailbreak templates are available during training. This setting better reflects real-world scenarios where new attacks continually emerge and evolve. To address this challenge, we propose a layer-wise, module-wise, and token-wise amplification framework that progressively magnifies internal feature discrepancies between benign and jailbreak prompts. We uncover safety-relevant layers, identify specific modules that inherently encode zero-shot discriminative signals, and localize informative safety tokens. Building upon these insights, we introduce ALERT (Amplification-based Jailbreak Detector), an efficient and effective zero-shot jailbreak detector that introduces two independent yet complementary classifiers on amplified representations. Extensive experiments on three safety benchmarks demonstrate that ALERT achieves consistently strong zero-shot detection performance. Specifically, (i) across all datasets and attack strategies, ALERT reliably ranks among the top two methods, and (ii) it outperforms the second-best baseline by at least 10% in average Accuracy and F1-score, and sometimes by up to 40%.

