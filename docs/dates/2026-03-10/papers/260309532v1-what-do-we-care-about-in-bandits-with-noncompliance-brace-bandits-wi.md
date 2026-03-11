---
layout: default
title: What Do We Care About in Bandits with Noncompliance? BRACE: Bandits with Recommendations, Abstention, and Certified Effects
---

# What Do We Care About in Bandits with Noncompliance? BRACE: Bandits with Recommendations, Abstention, and Certified Effects
**arXiv**：[2603.09532v1](https://arxiv.org/abs/2603.09532) · [PDF](https://arxiv.org/pdf/2603.09532.pdf)  
**作者**：Nicolás Della Penna  

**一句话要点**：提出BRACE算法，解决非合规多臂老虎机中目标选择问题，实现推荐与治疗策略的固定差距识别。

**关键词**：非合规多臂老虎机, 推荐策略, 治疗策略, 固定差距识别, 结构区间, 正交评分

## 3 点简述
- 核心问题：非合规老虎机中学习目标需选择，推荐福利与治疗学习目标可能不一致。
- 方法要点：BRACE为无参数阶段加倍算法，通过矩阵认证和结构区间实现策略值有效性。
- 实验效果：在多种场景下验证安全性，如弱识别下的弃权和宽区间、同质性失败时推荐福利优势。

## 摘要（原文）

> Bandits with noncompliance separate the learner's recommendation from the treatment actually delivered, so the learning target itself must be chosen. A platform may care about recommendation welfare in the current mediated workflow, treatment learning for a future direct-control regime, or anytime-valid uncertainty for one of those targets. These objectives need not agree. We formalize this objective-choice problem, identify the direct-control regime in which recommendation and treatment objectives collapse, and show by example that recommendation welfare can strictly exceed every learner-measurable treatment policy when downstream actors use private information. For finite-context square-IV problems we propose BRACE, a parameter-free phase-doubling algorithm that performs IV inversion only after matrix certification and otherwise returns full-range but honest structural intervals. BRACE delivers simultaneous policy-value validity, fixed-gap identification of the operationally optimal recommendation policy, and fixed-gap identification of the structurally optimal treatment policy under contextual homogeneity and invertibility. We complement the theory with a finite-context empirical benchmark spanning direct control, mediated present-versus-future tradeoffs, weak identification, homogeneity failure, and rectangular overidentification. The experiments show that safety appears as regret on easy problems, as abstention and wide valid intervals under weak identification, as a reason to prefer recommendation welfare under homogeneity failure, and as tighter structural uncertainty when extra instruments are available. For rich contexts, we also derive an orthogonal score whose conditional bias factorizes into compliance-model and outcome-model errors, clarifying what must be stabilized for anytime-valid semiparametric IV inference.

