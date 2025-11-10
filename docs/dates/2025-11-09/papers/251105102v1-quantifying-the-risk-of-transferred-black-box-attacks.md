---
layout: default
title: Quantifying the Risk of Transferred Black Box Attacks
---

# Quantifying the Risk of Transferred Black Box Attacks
**arXiv**：[2511.05102v1](https://arxiv.org/abs/2511.05102) · [PDF](https://arxiv.org/pdf/2511.05102.pdf)  
**作者**：Disesdi Susanna Cox, Niklas Bunzel  

**一句话要点**：提出基于CKA相似性的目标测试框架以量化黑盒转移攻击风险

**关键词**：黑盒对抗攻击, 转移攻击风险, CKA相似性, 代理模型, 回归估计器, 安全测试

## 3 点简述
- 核心问题：黑盒转移攻击风险难以准确量化，高维输入空间测试不现实。
- 方法要点：利用高/低CKA相似性的代理模型优化对抗子空间覆盖。
- 实验或效果：使用回归估计器提供可操作的风险量化，未知具体效果。

## 摘要（原文）

> Neural networks have become pervasive across various applications, including
> security-related products. However, their widespread adoption has heightened
> concerns regarding vulnerability to adversarial attacks. With emerging
> regulations and standards emphasizing security, organizations must reliably
> quantify risks associated with these attacks, particularly regarding
> transferred adversarial attacks, which remain challenging to evaluate
> accurately. This paper investigates the complexities involved in resilience
> testing against transferred adversarial attacks. Our analysis specifically
> addresses black-box evasion attacks, highlighting transfer-based attacks due to
> their practical significance and typically high transferability between neural
> network models. We underline the computational infeasibility of exhaustively
> exploring high-dimensional input spaces to achieve complete test coverage. As a
> result, comprehensive adversarial risk mapping is deemed impractical. To
> mitigate this limitation, we propose a targeted resilience testing framework
> that employs surrogate models strategically selected based on Centered Kernel
> Alignment (CKA) similarity. By leveraging surrogate models exhibiting both high
> and low CKA similarities relative to the target model, the proposed approach
> seeks to optimize coverage of adversarial subspaces. Risk estimation is
> conducted using regression-based estimators, providing organizations with
> realistic and actionable risk quantification.

