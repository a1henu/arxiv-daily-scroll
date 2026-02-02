---
layout: default
title: Toward Non-Expert Customized Congestion Control
---

# Toward Non-Expert Customized Congestion Control
**arXiv**：[2601.22461v1](https://arxiv.org/abs/2601.22461) · [PDF](https://arxiv.org/pdf/2601.22461.pdf)  
**作者**：Mingrui Zhang, Hamid Bagheri, Lisong Xu  

**一句话要点**：提出NECC框架以解决非专家用户定制拥塞控制算法的实现难题

**关键词**：拥塞控制算法, 非专家定制, 大语言模型, BPF接口, 网络性能优化

## 3 点简述
- 通用拥塞控制算法难以满足用户特定需求，但非专家用户缺乏定制实现的专业知识
- NECC框架利用大语言模型和BPF接口，帮助非专家用户轻松建模、实现和部署定制算法
- 评估显示NECC性能良好，并讨论了相关见解和未来研究方向

## 摘要（原文）

> General-purpose congestion control algorithms (CCAs) are designed to achieve general congestion control goals, but they may not meet the specific requirements of certain users. Customized CCAs can meet certain users' specific requirements; however, non-expert users often lack the expertise to implement them. In this paper, we present an exploratory non-expert customized CCA framework, named NECC, which enables non-expert users to easily model, implement, and deploy their customized CCAs by leveraging Large Language Models and the Berkeley Packet Filter (BPF) interface. To the best of our knowledge, we are the first to address the customized CCA implementation problem. Our evaluations using real-world CCAs show that the performance of NECC is very promising, and we discuss the insights that we find and possible future research directions.

