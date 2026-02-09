---
layout: default
title: Next-generation cyberattack detection with large language models: anomaly analysis across heterogeneous logs
---

# Next-generation cyberattack detection with large language models: anomaly analysis across heterogeneous logs
**arXiv**：[2602.06777v1](https://arxiv.org/abs/2602.06777) · [PDF](https://arxiv.org/pdf/2602.06777.pdf)  
**作者**：Yassine Chagna, Antal Goldschmidt  

**一句话要点**：提出基于大语言模型的异构日志异常检测框架，解决传统入侵检测系统误报率高、语义盲区及数据稀缺问题。

**关键词**：大语言模型, 异常检测, 异构日志, 知识蒸馏, 数据集构建, 入侵检测系统

## 3 点简述
- 核心问题：传统入侵检测系统存在高误报率、语义盲区和数据稀缺，因日志敏感导致干净数据集罕见。
- 方法要点：贡献包括LogAtlas数据集、实证基准测试揭示标准指标误导性，以及两阶段训练框架结合日志理解与实时检测。
- 实验或效果：结果展示实际可行性，推理时间0.3-0.5秒每会话，运营成本低于50美元每天。

## 摘要（原文）

> This project explores large language models (LLMs) for anomaly detection across heterogeneous log sources. Traditional intrusion detection systems suffer from high false positive rates, semantic blindness, and data scarcity, as logs are inherently sensitive, making clean datasets rare. We address these challenges through three contributions: (1) LogAtlas-Foundation-Sessions and LogAtlas-Defense-Set, balanced and heterogeneous log datasets with explicit attack annotations and privacy preservation; (2) empirical benchmarking revealing why standard metrics such as F1 and accuracy are misleading for security applications; and (3) a two phase training framework combining log understanding (Base-AMAN, 3B parameters) with real time detection (AMAN, 0.5B parameters via knowledge distillation). Results demonstrate practical feasibility, with inference times of 0.3-0.5 seconds per session and operational costs below 50 USD per day.

