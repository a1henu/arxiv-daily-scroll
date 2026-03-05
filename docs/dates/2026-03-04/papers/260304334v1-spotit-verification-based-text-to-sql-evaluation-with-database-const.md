---
layout: default
title: SpotIt+: Verification-based Text-to-SQL Evaluation with Database Constraints
---

# SpotIt+: Verification-based Text-to-SQL Evaluation with Database Constraints
**arXiv**：[2603.04334v1](https://arxiv.org/abs/2603.04334) · [PDF](https://arxiv.org/pdf/2603.04334.pdf)  
**作者**：Rocky Klopfenstein, Yang He, Andrew Tremante, Yuepeng Wang, Nina Narodytska, Haoze Wu  

**一句话要点**：提出SpotIt+工具，通过有界等价验证评估Text-to-SQL系统，结合约束挖掘提升反例真实性。

**关键词**：Text-to-SQL评估, 有界等价验证, 约束挖掘, 反例生成, 数据库实例搜索

## 3 点简述
- 核心问题：标准测试评估可能遗漏生成SQL与真实查询间的差异，需更有效验证方法。
- 方法要点：基于有界等价验证主动搜索区分查询的数据库实例，引入约束挖掘管道确保反例相关性。
- 实验或效果：在BIRD数据集上，约束挖掘使SpotIt+生成更真实反例，高效揭示更多差异。

## 摘要（原文）

> We present SpotIt+, an open-source tool for evaluating Text-to-SQL systems via bounded equivalence verification. Given a generated SQL query and the ground truth, SpotIt+ actively searches for database instances that differentiate the two queries. To ensure that the generated counterexamples reflect practically relevant discrepancies, we introduce a constraint-mining pipeline that combines rule-based specification mining over example databases with LLM-based validation. Experimental results on the BIRD dataset show that the mined constraints enable SpotIt+ to generate more realistic differentiating databases, while preserving its ability to efficiently uncover numerous discrepancies between generated and gold SQL queries that are missed by standard test-based evaluation.

