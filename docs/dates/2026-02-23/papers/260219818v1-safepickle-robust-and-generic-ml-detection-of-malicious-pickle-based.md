---
layout: default
title: SafePickle: Robust and Generic ML Detection of Malicious Pickle-based ML Models
---

# SafePickle: Robust and Generic ML Detection of Malicious Pickle-based ML Models
**arXiv**：[2602.19818v1](https://arxiv.org/abs/2602.19818) · [PDF](https://arxiv.org/pdf/2602.19818.pdf)  
**作者**：Hillel Ohayon, Daniel Gilkarov, Ran Dubin  

**一句话要点**：提出基于机器学习的轻量级扫描器SafePickle，以检测恶意Pickle序列化模型文件

**关键词**：恶意模型检测, Pickle安全, 机器学习扫描器, 远程代码执行, 静态特征提取, 库无关检测

## 3 点简述
- 核心问题：Python pickle格式序列化的模型文件在加载时存在远程代码执行风险，现有防御方法依赖复杂策略生成，可扩展性差。
- 方法要点：从Pickle字节码静态提取结构和语义特征，应用监督和无监督模型进行分类，无需策略生成或代码插桩。
- 实验或效果：在多个数据集上评估，F1分数达90.01%，优于现有扫描器，并能正确检测9/9高级规避恶意模型。

## 摘要（原文）

> Model repositories such as Hugging Face increasingly distribute machine learning artifacts serialized with Python's pickle format, exposing users to remote code execution (RCE) risks during model loading. Recent defenses, such as PickleBall, rely on per-library policy synthesis that requires complex system setups and verified benign models, which limits scalability and generalization. In this work, we propose a lightweight, machine-learning-based scanner that detects malicious Pickle-based files without policy generation or code instrumentation. Our approach statically extracts structural and semantic features from Pickle bytecode and applies supervised and unsupervised models to classify files as benign or malicious. We construct and release a labeled dataset of 727 Pickle-based files from Hugging Face and evaluate our models on four datasets: our own, PickleBall (out-of-distribution), Hide-and-Seek (9 advanced evasive malicious models), and synthetic joblib files. Our method achieves 90.01% F1-score compared with 7.23%-62.75% achieved by the SOTA scanners (Modelscan, Fickling, ClamAV, VirusTotal) on our dataset. Furthermore, on the PickleBall data (OOD), it achieves 81.22% F1-score compared with 76.09% achieved by the PickleBall method, while remaining fully library-agnostic. Finally, we show that our method is the only one to correctly parse and classify 9/9 evasive Hide-and-Seek malicious models specially crafted to evade scanners. This demonstrates that data-driven detection can effectively and generically mitigate Pickle-based model file attacks.

