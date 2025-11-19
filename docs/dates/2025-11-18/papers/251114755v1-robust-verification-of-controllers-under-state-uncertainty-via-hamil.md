---
layout: default
title: Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis
---

# Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis
**arXiv**：[2511.14755v1](https://arxiv.org/abs/2511.14755) · [PDF](https://arxiv.org/pdf/2511.14755.pdf)  
**作者**：Albert Lin, Alessandro Pinto, Somil Bansal  

**一句话要点**：提出RoVer-CoRe框架，通过Hamilton-Jacobi可达性分析验证感知不确定性下控制器的安全性。

**关键词**：Hamilton-Jacobi可达性分析, 控制器安全验证, 感知不确定性, 非线性系统, 形式化验证

## 3 点简述
- 核心问题：感知不确定性下非线性控制器安全验证困难，现有方法保守或受限。
- 方法要点：将控制器、观测和状态估计串联，构建等效闭环系统以兼容可达性分析。
- 实验或效果：在飞机滑行和神经网络漫游车导航案例中验证框架有效性。

## 摘要（原文）

> As perception-based controllers for autonomous systems become increasingly popular in the real world, it is important that we can formally verify their safety and performance despite perceptual uncertainty. Unfortunately, the verification of such systems remains challenging, largely due to the complexity of the controllers, which are often nonlinear, nonconvex, learning-based, and/or black-box. Prior works propose verification algorithms that are based on approximate reachability methods, but they often restrict the class of controllers and systems that can be handled or result in overly conservative analyses. Hamilton-Jacobi (HJ) reachability analysis is a popular formal verification tool for general nonlinear systems that can compute optimal reachable sets under worst-case system uncertainties; however, its application to perception-based systems is currently underexplored. In this work, we propose RoVer-CoRe, a framework for the Robust Verification of Controllers via HJ Reachability. To the best of our knowledge, RoVer-CoRe is the first HJ reachability-based framework for the verification of perception-based systems under perceptual uncertainty. Our key insight is to concatenate the system controller, observation function, and the state estimation modules to obtain an equivalent closed-loop system that is readily compatible with existing reachability frameworks. Within RoVer-CoRe, we propose novel methods for formal safety verification and robust controller design. We demonstrate the efficacy of the framework in case studies involving aircraft taxiing and NN-based rover navigation. Code is available at the link in the footnote.

