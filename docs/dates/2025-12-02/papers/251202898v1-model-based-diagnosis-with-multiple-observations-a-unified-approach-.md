---
layout: default
title: Model-Based Diagnosis with Multiple Observations: A Unified Approach for C Software and Boolean Circuits
---

# Model-Based Diagnosis with Multiple Observations: A Unified Approach for C Software and Boolean Circuits
**arXiv**：[2512.02898v1](https://arxiv.org/abs/2512.02898) · [PDF](https://arxiv.org/pdf/2512.02898.pdf)  
**作者**：Pedro Orvalho, Marta Kwiatkowska, Mikoláš Janota, Vasco Manquinho  

**一句话要点**：提出CFaults工具，基于模型诊断与多观测统一方法，解决C软件和布尔电路多故障定位问题。

**关键词**：故障定位, 模型诊断, MaxSAT求解, C软件调试, 布尔电路, 多故障处理

## 3 点简述
- 核心问题：现有基于公式的故障定位方法在多故障场景下无法保证跨测试一致性或产生冗余诊断。
- 方法要点：利用模型诊断整合多观测，构建统一MaxSAT公式，确保诊断一致性和子集最小化。
- 实验效果：在C软件基准上速度优于BugAssist等工具，在布尔电路基准上保持竞争力，仅产生最小诊断集。

## 摘要（原文）

> Debugging is one of the most time-consuming and expensive tasks in software development and circuit design. Several formula-based fault localisation (FBFL) methods have been proposed, but they fail to guarantee a set of diagnoses across all failing tests or may produce redundant diagnoses that are not subset-minimal, particularly for programs/circuits with multiple faults.
>   This paper introduces CFaults, a novel fault localisation tool for C software and Boolean circuits with multiple faults. CFaults leverages Model-Based Diagnosis (MBD) with multiple observations and aggregates all failing test cases into a unified Maximum Satisfiability (MaxSAT) formula. Consequently, our method guarantees consistency across observations and simplifies the fault localisation procedure. Experimental results on three benchmark sets, two of C programs, TCAS and C-Pack-IPAs, and one of Boolean circuits, ISCAS85, show that CFaults is faster at localising faults in C software than other FBFL approaches such as BugAssist, SNIPER, and HSD. On the ISCAS85 benchmark, CFaults is generally slower than HSD; however, it localises faults in only 6% fewer circuits, demonstrating that it remains competitive in this domain. Furthermore, CFaults produces only subset-minimal diagnoses of faulty statements, whereas the other approaches tend to enumerate redundant diagnoses (e.g., BugAssist and SNIPER).

