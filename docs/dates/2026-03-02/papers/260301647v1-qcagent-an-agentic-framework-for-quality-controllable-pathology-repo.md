---
layout: default
title: QCAgent: An agentic framework for quality-controllable pathology report generation from whole slide image
---

# QCAgent: An agentic framework for quality-controllable pathology report generation from whole slide image
**arXiv**：[2603.01647v1](https://arxiv.org/abs/2603.01647) · [PDF](https://arxiv.org/pdf/2603.01647.pdf)  
**作者**：Rundong Wang, Wei Ba, Ying Zhou, Yingtai Li, Bowen Liu, Baizhi Wang, Yuhao Wang, Zhidong Yang, Kun Zhang, Rui Yan, S. Kevin Zhou  

**一句话要点**：提出QCAgent框架，通过代理机制实现从全切片图像生成质量可控的病理报告。

**关键词**：病理报告生成, 全切片图像分析, 代理框架, 质量控制, 视觉证据定位

## 3 点简述
- 现有方法生成病理报告时缺乏细粒度视觉证据定位和质量控制。
- QCAgent引入用户定义清单引导的批判机制和基于文本-补丁语义检索的区域重识别。
- 实验表明该框架能生成临床意义强、覆盖全面的可控病理报告。

## 摘要（原文）

> Recent methods for pathology report generation from whole-slide image (WSI) are capable of producing slide-level diagnostic descriptions but fail to ground fine-grained statements in localized visual evidence. Furthermore, they lack control over which diagnostic details to include and how to verify them. Inspired by emerging agentic analysis paradigms and the diagnostic workflow of pathologists,who selectively examine multiple fields of view, we propose QCAgent, an agentic framework for quality-controllable WSI report generation. The core innovations of this framework are as follows: (i) it incorporates a customized critique mechanism guided by a user-defined checklist specifying required diagnostic details and constraints; (ii) it re-identifies informative regions in the WSI based on the critique feedback and text-patch semantic retrieval, a process that iteratively enriches and reconciles the report. Experiments demonstrate that by making report requirements explicitly prompt-defined, constraint-aware, and verifiable through evidence-grounded refinement, QCAgent enables controllable generation of clinically meaningful and high-coverage pathology reports from WSI.

