---
layout: default
title: Defining Operational Conditions for Safety-Critical AI-Based Systems from Data
---

# Defining Operational Conditions for Safety-Critical AI-Based Systems from Data
**arXiv**：[2601.22118v1](https://arxiv.org/abs/2601.22118) · [PDF](https://arxiv.org/pdf/2601.22118.pdf)  
**作者**：Johann Christensen, Elena Hoemann, Frank Köster, Sven Hallerbach  

**一句话要点**：提出基于多维核表示的后验方法，从数据定义安全关键AI系统的操作设计域。

**关键词**：操作设计域定义, 安全关键AI系统, 多维核表示, 后验方法, 数据驱动认证

## 3 点简述
- 核心问题：安全关键AI系统需定义操作设计域，但复杂环境或现有数据下定义困难。
- 方法要点：采用多维核表示，从收集的数据中后验推导操作设计域，支持安全设计。
- 实验或效果：通过蒙特卡洛方法和真实航空用例验证，证明数据驱动操作设计域可等于隐藏真实域。

## 摘要（原文）

> Artificial Intelligence (AI) has been on the rise in many domains, including numerous safety-critical applications. However, for complex systems found in the real world, or when data already exist, defining the underlying environmental conditions is extremely challenging. This often results in an incomplete description of the environment in which the AI-based system must operate. Nevertheless, this description, called the Operational Design Domain (ODD), is required in many domains for the certification of AI-based systems. Traditionally, the ODD is created in the early stages of the development process, drawing on sophisticated expert knowledge and related standards. This paper presents a novel Safety-by-Design method to a posteriori define the ODD from previously collected data using a multi-dimensional kernel-based representation. This approach is validated through both Monte Carlo methods and a real-world aviation use case for a future safety-critical collision-avoidance system. Moreover, by defining under what conditions two ODDs are equal, the paper shows that the data-driven ODD can equal the original, underlying hidden ODD of the data. Utilizing the novel, Safe-by-Design kernel-based ODD enables future certification of data-driven, safety-critical AI-based systems.

