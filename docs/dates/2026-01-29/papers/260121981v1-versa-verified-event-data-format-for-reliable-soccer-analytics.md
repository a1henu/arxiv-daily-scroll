---
layout: default
title: VERSA: Verified Event Data Format for Reliable Soccer Analytics
---

# VERSA: Verified Event Data Format for Reliable Soccer Analytics
**arXiv**：[2601.21981v1](https://arxiv.org/abs/2601.21981) · [PDF](https://arxiv.org/pdf/2601.21981.pdf)  
**作者**：Geonhee Jo, Mingu Kang, Kangmin Lee, Minho Lee, Pascal Bauer, Sang-Ki Ko  

**一句话要点**：提出VERSA验证框架以解决足球事件流数据中的逻辑不一致问题

**关键词**：事件流数据验证, 足球数据分析, 状态转移模型, 数据完整性, 逻辑一致性检测

## 3 点简述
- 核心问题：事件流数据存在逻辑不一致（如事件顺序错误或缺失），影响分析可靠性
- 方法要点：基于状态转移模型定义有效事件序列，自动检测和纠正异常模式
- 实验或效果：在K联赛数据中检测到18.81%不一致，提升跨提供商一致性和下游任务性能

## 摘要（原文）

> Event stream data is a critical resource for fine-grained analysis across various domains, including financial transactions, system operations, and sports. In sports, it is actively used for fine-grained analyses such as quantifying player contributions and identifying tactical patterns. However, the reliability of these models is fundamentally limited by inherent data quality issues that cause logical inconsistencies (e.g., incorrect event ordering or missing events). To this end, this study proposes VERSA (Verified Event Data Format for Reliable Soccer Analytics), a systematic verification framework that ensures the integrity of event stream data within the soccer domain. VERSA is based on a state-transition model that defines valid event sequences, thereby enabling the automatic detection and correction of anomalous patterns within the event stream data. Notably, our examination of event data from the K League 1 (2024 season), provided by Bepro, detected that 18.81% of all recorded events exhibited logical inconsistencies. Addressing such integrity issues, our experiments demonstrate that VERSA significantly enhances cross-provider consistency, ensuring stable and unified data representation across heterogeneous sources. Furthermore, we demonstrate that data refined by VERSA significantly improves the robustness and performance of a downstream task called VAEP, which evaluates player contributions. These results highlight that the verification process is highly effective in increasing the reliability of data-driven analysis.

