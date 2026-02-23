---
layout: default
title: FENCE: A Financial and Multimodal Jailbreak Detection Dataset
---

# FENCE: A Financial and Multimodal Jailbreak Detection Dataset
**arXiv**：[2602.18154v1](https://arxiv.org/abs/2602.18154) · [PDF](https://arxiv.org/pdf/2602.18154.pdf)  
**作者**：Mirae Kim, Seonghun Jeong, Youngjun Kwak  

**一句话要点**：提出FENCE数据集以解决金融领域多模态越狱检测资源稀缺问题

**关键词**：多模态越狱检测, 金融数据集, 双语数据集, 图像威胁, 基线检测器, 领域真实性

## 3 点简述
- 核心问题：多模态大模型在金融应用中面临越狱攻击风险，现有检测资源不足
- 方法要点：构建双语多模态数据集，结合金融查询与图像威胁以增强领域真实性
- 实验或效果：基线检测器在内部数据上达99%准确率，并在外部基准上保持强性能

## 摘要（原文）

> Jailbreaking poses a significant risk to the deployment of Large Language Models (LLMs) and Vision Language Models (VLMs). VLMs are particularly vulnerable because they process both text and images, creating broader attack surfaces. However, available resources for jailbreak detection are scarce, particularly in finance. To address this gap, we present FENCE, a bilingual (Korean-English) multimodal dataset for training and evaluating jailbreak detectors in financial applications. FENCE emphasizes domain realism through finance-relevant queries paired with image-grounded threats. Experiments with commercial and open-source VLMs reveal consistent vulnerabilities, with GPT-4o showing measurable attack success rates and open-source models displaying greater exposure. A baseline detector trained on FENCE achieves 99 percent in-distribution accuracy and maintains strong performance on external benchmarks, underscoring the dataset's robustness for training reliable detection models. FENCE provides a focused resource for advancing multimodal jailbreak detection in finance and for supporting safer, more reliable AI systems in sensitive domains. Warning: This paper includes example data that may be offensive.

