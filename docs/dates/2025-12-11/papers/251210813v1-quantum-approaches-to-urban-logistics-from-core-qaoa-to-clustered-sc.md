---
layout: default
title: Quantum Approaches to Urban Logistics: From Core QAOA to Clustered Scalability
---

# Quantum Approaches to Urban Logistics: From Core QAOA to Clustered Scalability
**arXiv**：[2512.10813v1](https://arxiv.org/abs/2512.10813) · [PDF](https://arxiv.org/pdf/2512.10813.pdf)  
**作者**：F. Picariello, G. Turati, R. Antonelli, I. Bailo, S. Bonura, G. Ciarfaglia, S. Cipolla, P. Cremonesi, M. Ferrari Dacrema, M. Gabusi, I. Gentile, V. Morreale, A. Noto  

**一句话要点**：提出聚类QAOA以解决带约束旅行商问题的量子优化可扩展性挑战

**关键词**：量子近似优化算法, 旅行商问题, 物流优化, 量子计算, 约束优化, 可扩展性

## 3 点简述
- 研究量子近似优化算法在带现实约束旅行商问题中的应用潜力
- 采用QUBO建模整合车辆容量、道路可达性和时间窗口等物流约束
- 提出聚类QAOA方法，通过分解大实例提升量子硬件有限下的可扩展性

## 摘要（原文）

> The Traveling Salesman Problem (TSP) is a fundamental challenge in combinatorial optimization, widely applied in logistics and transportation. As the size of TSP instances grows, traditional algorithms often struggle to produce high-quality solutions within reasonable timeframes. This study investigates the potential of the Quantum Approximate Optimization Algorithm (QAOA), a hybrid quantum-classical method, to solve TSP under realistic constraints. We adopt a QUBO-based formulation of TSP that integrates real-world logistical constraints reflecting operational conditions, such as vehicle capacity, road accessibility, and time windows, while ensuring compatibility with the limitations of current quantum hardware. Our experiments are conducted in a simulated environment using high-performance computing (HPC) resources to assess QAOA's performance across different problem sizes and quantum circuit depths. In order to improve scalability, we propose clustering QAOA (Cl-QAOA), a hybrid approach combining classical machine learning with QAOA. This method decomposes large TSP instances into smaller sub-problems, making quantum optimization feasible even on devices with a limited number of qubits. The results offer a comprehensive evaluation of QAOA's strengths and limitations in solving constrained TSP scenarios. This study advances quantum optimization and lays groundwork for future large-scale applications.

