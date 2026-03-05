---
layout: default
title: Lambdas at the Far Edge: a Tale of Flying Lambdas and Lambdas on Wheels
---

# Lambdas at the Far Edge: a Tale of Flying Lambdas and Lambdas on Wheels
**arXiv**：[2603.04008v1](https://arxiv.org/abs/2603.04008) · [PDF](https://arxiv.org/pdf/2603.04008.pdf)  
**作者**：Giorgio Audrito, Daniele Bortoluzzi, Ferruccio Damiani, Giordano Scarso, Gianluca Torta, Andrea Basso, Monica Cochi, Lorenzo Gusman, Lorenzo Comba, Paolo Gay, Paola Dal Zovo, Giada Galati, Francesco Gallo, Aljaž Grdadolnik, Massimo Pescarollo, Paola Pisano  

**一句话要点**：提出基于交换演算的聚合编程框架FCPP，用于网络远边缘设备如漫游车和无人机的集体行为编程。

**关键词**：聚合编程, 交换演算, lambda演算, 网络远边缘, 分布式系统, C++库

## 3 点简述
- 核心问题：网络远边缘分布式设备的集体行为编程，依赖异步邻近交互。
- 方法要点：基于交换演算（XC）的聚合编程范式，扩展lambda演算以提供隐式通信机制。
- 实验或效果：实现为C++库FCPP，已部署于漫游车，计划用于无人机。

## 摘要（原文）

> Aggregate Programming (AP) is a paradigm for programming the collective behaviour of sets of distributed devices, possibly situated at the network far edge, by relying on asynchronous proximity-based interactions. The eXchange Calculus (XC), a recently proposed foundational model for AP, is essentially a typed lambda calculus extended with an operator (the exchange operator) providing an implicit communication mechanism between neighbour devices. This paper provides a gentle introduction to XC and to its implementation as a C++ library, called FCPP. The FCPP library and toolchain has been mainly developed at the Department of Computer Science of the University of Turin, where Stefano Berardi spent most of his academic career conducting outstanding research about logical foundation of computer science and transmitting his passion for research to students and young researchers, often exploiting typed lambda calculi. An FCCP program is essentially a typed lambda term, and FCPP has been used to write code that has been deployed on devices at the far edge of the network, including rovers and (soon) Uncrewed Aerial Vehicles (UAVs); hence the title of the paper.

