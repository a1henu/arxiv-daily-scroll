---
layout: default
title: TeleDoCTR: Domain-Specific and Contextual Troubleshooting for Telecommunications
---

# TeleDoCTR: Domain-Specific and Contextual Troubleshooting for Telecommunications
**arXiv**：[2601.00691v1](https://arxiv.org/abs/2601.00691) · [PDF](https://arxiv.org/pdf/2601.00691.pdf)  
**作者**：Mohamed Trabelsi, Huseyin Uzunalioglu  

**一句话要点**：提出TeleDoCTR系统，用于电信领域端到端工单故障排除，提升效率与准确性。

**关键词**：电信故障排除, 工单分类, 上下文检索, 报告生成, 领域特定模型

## 3 点简述
- 核心问题：电信工单故障排除依赖专家手动处理，耗时且效率低。
- 方法要点：集成领域特定排序和生成模型，自动化分类、检索和报告生成任务。
- 实验或效果：在真实电信数据集上评估，性能优于现有方法，显著提升准确性和效率。

## 摘要（原文）

> Ticket troubleshooting refers to the process of analyzing and resolving problems that are reported through a ticketing system. In large organizations offering a wide range of services, this task is highly complex due to the diversity of submitted tickets and the need for specialized domain knowledge. In particular, troubleshooting in telecommunications (telecom) is a very time-consuming task as it requires experts to interpret ticket content, consult documentation, and search historical records to identify appropriate resolutions. This human-intensive approach not only delays issue resolution but also hinders overall operational efficiency. To enhance the effectiveness and efficiency of ticket troubleshooting in telecom, we propose TeleDoCTR, a novel telecom-related, domain-specific, and contextual troubleshooting system tailored for end-to-end ticket resolution in telecom. TeleDoCTR integrates both domain-specific ranking and generative models to automate key steps of the troubleshooting workflow which are: routing tickets to the appropriate expert team responsible for resolving the ticket (classification task), retrieving contextually and semantically similar historical tickets (retrieval task), and generating a detailed fault analysis report outlining the issue, root cause, and potential solutions (generation task). We evaluate TeleDoCTR on a real-world dataset from a telecom infrastructure and demonstrate that it achieves superior performance over existing state-of-the-art methods, significantly enhancing the accuracy and efficiency of the troubleshooting process.

