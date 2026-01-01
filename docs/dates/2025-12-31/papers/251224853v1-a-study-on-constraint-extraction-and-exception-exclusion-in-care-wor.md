---
layout: default
title: A study on constraint extraction and exception exclusion in care worker scheduling
---

# A study on constraint extraction and exception exclusion in care worker scheduling
**arXiv**：[2512.24853v1](https://arxiv.org/abs/2512.24853) · [PDF](https://arxiv.org/pdf/2512.24853.pdf)  
**作者**：Koki Suenaga, Tomohiro Furuta, Satoshi Ono  

**一句话要点**：提出基于约束模板与例外排除的护工排班方法，以应对养老院个性化需求。

**关键词**：护工排班, 约束提取, 例外排除, 约束编程, 养老院管理

## 3 点简述
- 核心问题：养老院排班需定制化约束，现有技术难以自动提取并排除例外约束。
- 方法要点：利用约束模板提取组合条件，并加入机制排除例外约束，支持约束编程求解。
- 实验或效果：实验显示方法成功生成满足硬约束的排班，并减少软约束违规。

## 摘要（原文）

> Technologies for automatically generating work schedules have been extensively studied; however, in long-term care facilities, the conditions vary between facilities, making it essential to interview the managers who create shift schedules to design facility-specific constraint conditions. The proposed method utilizes constraint templates to extract combinations of various components, such as shift patterns for consecutive days or staff combinations. The templates can extract a variety of constraints by changing the number of days and the number of staff members to focus on and changing the extraction focus to patterns or frequency. In addition, unlike existing constraint extraction techniques, this study incorporates mechanisms to exclude exceptional constraints. The extracted constraints can be employed by a constraint programming solver to create care worker schedules. Experiments demonstrated that our proposed method successfully created schedules that satisfied all hard constraints and reduced the number of violations for soft constraints by circumventing the extraction of exceptional constraints.

