---
layout: default
title: SecCodeBench-V2 Technical Report
---

# SecCodeBench-V2 Technical Report
**arXiv**：[2602.15485v1](https://arxiv.org/abs/2602.15485) · [PDF](https://arxiv.org/pdf/2602.15485.pdf)  
**作者**：Longfei Chen, Ji Zhao, Lanxiao Cui, Tong Su, Xingbo Pan, Ziyang Li, Yongxing Wu, Qijiang Cao, Qiyao Cai, Jing Zhang, Yuandong Ni, Junyao He, Zeyu Zhang, Chao Ge, Xuhuai Lu, Zeyu Gao, Yuxin Cui, Weisen Chen, Yuxuan Peng, Shengping Wang, Qi Li, Yukai Huang, Yukun Liu, Tuo Zhou, Terry Yue Zhuo, Junyang Lin, Chao Zhang  

**一句话要点**：提出SecCodeBench-V2基准，用于评估大语言模型生成安全代码的能力。

**关键词**：代码安全基准, 大语言模型评估, 动态执行验证, 工业场景测试, 多语言漏洞覆盖

## 3 点简述
- 核心问题：评估AI编程助手生成安全代码的能力，覆盖22种CWE漏洞类型和5种编程语言。
- 方法要点：基于阿里巴巴工业场景构建98个函数级生成与修复任务，提供可执行的PoC测试用例进行动态验证。
- 实验或效果：设计基于Pass@K的评分协议，通过隔离环境执行和LLM裁判实现可复现的评估。

## 摘要（原文）

> We introduce SecCodeBench-V2, a publicly released benchmark for evaluating Large Language Model (LLM) copilots' capabilities of generating secure code. SecCodeBench-V2 comprises 98 generation and fix scenarios derived from Alibaba Group's industrial productions, where the underlying security issues span 22 common CWE (Common Weakness Enumeration) categories across five programming languages: Java, C, Python, Go, and Node.js. SecCodeBench-V2 adopts a function-level task formulation: each scenario provides a complete project scaffold and requires the model to implement or patch a designated target function under fixed interfaces and dependencies. For each scenario, SecCodeBench-V2 provides executable proof-of-concept (PoC) test cases for both functional validation and security verification. All test cases are authored and double-reviewed by security experts, ensuring high fidelity, broad coverage, and reliable ground truth. Beyond the benchmark itself, we build a unified evaluation pipeline that assesses models primarily via dynamic execution. For most scenarios, we compile and run model-generated artifacts in isolated environments and execute PoC test cases to validate both functional correctness and security properties. For scenarios where security issues cannot be adjudicated with deterministic test cases, we additionally employ an LLM-as-a-judge oracle. To summarize performance across heterogeneous scenarios and difficulty levels, we design a Pass@K-based scoring protocol with principled aggregation over scenarios and severity, enabling holistic and comparable evaluation across models. Overall, SecCodeBench-V2 provides a rigorous and reproducible foundation for assessing the security posture of AI coding assistants, with results and artifacts released at https://alibaba.github.io/sec-code-bench. The benchmark is publicly available at https://github.com/alibaba/sec-code-bench.

