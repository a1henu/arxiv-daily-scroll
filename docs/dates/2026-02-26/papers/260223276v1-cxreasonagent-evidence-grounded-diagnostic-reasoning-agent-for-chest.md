---
layout: default
title: CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays
---

# CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays
**arXiv**：[2602.23276v1](https://arxiv.org/abs/2602.23276) · [PDF](https://arxiv.org/pdf/2602.23276.pdf)  
**作者**：Hyungyung Lee, Hangyul Yoon, Edward Choi  

**一句话要点**：提出CXReasonAgent以解决胸片诊断中视觉语言模型证据不足和适应性差的问题

**关键词**：胸片诊断, 证据推理, 多轮对话, 临床工具集成, 视觉语言模型

## 3 点简述
- 核心问题：大型视觉语言模型在胸片诊断中生成响应缺乏可靠证据，且难以适应新任务
- 方法要点：集成大语言模型与临床诊断工具，基于图像证据进行多步推理
- 实验或效果：在CXReasonDial基准上验证，生成更可靠和可验证的诊断响应

## 摘要（原文）

> Chest X-ray plays a central role in thoracic diagnosis, and its interpretation inherently requires multi-step, evidence-grounded reasoning. However, large vision-language models (LVLMs) often generate plausible responses that are not faithfully grounded in diagnostic evidence and provide limited visual evidence for verification, while also requiring costly retraining to support new diagnostic tasks, limiting their reliability and adaptability in clinical settings. To address these limitations, we present CXReasonAgent, a diagnostic agent that integrates a large language model (LLM) with clinically grounded diagnostic tools to perform evidence-grounded diagnostic reasoning using image-derived diagnostic and visual evidence. To evaluate these capabilities, we introduce CXReasonDial, a multi-turn dialogue benchmark with 1,946 dialogues across 12 diagnostic tasks, and show that CXReasonAgent produces faithfully grounded responses, enabling more reliable and verifiable diagnostic reasoning than LVLMs. These findings highlight the importance of integrating clinically grounded diagnostic tools, particularly in safety-critical clinical settings.

