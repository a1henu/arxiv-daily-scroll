---
layout: default
title: Physics-informed neural operator for predictive parametric phase-field modelling
---

# Physics-informed neural operator for predictive parametric phase-field modelling
**arXiv**：[2603.09693v1](https://arxiv.org/abs/2603.09693) · [PDF](https://arxiv.org/pdf/2603.09693.pdf)  
**作者**：Nanxi Chen, Airong Chen, Rujin Ma  

**一句话要点**：提出PF-PINO物理信息神经算子框架，以高效预测参数化相场建模中的材料演化

**关键词**：物理信息神经算子, 参数化相场建模, 材料演化预测, 科学机器学习, 傅里叶神经算子

## 3 点简述
- 相场建模预测材料演化计算成本高，传统神经算子缺乏物理约束影响泛化能力
- PF-PINO通过嵌入相场控制方程残差到损失函数，在训练中强制物理约束
- 在电化学腐蚀、枝晶凝固和旋节分解等基准问题上验证，PF-PINO在精度和稳定性上优于传统FNO

## 摘要（原文）

> Predicting the microstructural and morphological evolution of materials through phase-field modelling is computationally intensive, particularly for high-throughput parametric studies. While neural operators such as the Fourier neural operator (FNO) show promise in accelerating the solution of parametric partial differential equations (PDEs), the lack of explicit physical constraints, may limit generalisation and long-term accuracy for complex phase-field dynamics. Here, we develop a physics-informed neural operator framework to learn parametric phase-field PDEs, namely PF-PINO. By embedding the residuals of phase-field governing equations into the data-fidelity loss function, our framework effectively enforces physical constraints during training. We validate PF-PINO against benchmark phase-field problems, including electrochemical corrosion, dendritic crystal solidification, and spinodal decomposition. Our results demonstrate that PF-PINO significantly outperforms conventional FNO in accuracy, generalisation capability, and long-term stability. This work provides a robust and efficient computational tool for phase-field modelling and highlights the potential of physics-informed neural operators to advance scientific machine learning for complex interfacial evolution problems.

