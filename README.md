# Chatbot

一个用于构建与迭代聊天机器人的基础仓库。

## 当前可改进点（快速体检）

目前仓库只有一个最小化的 `README.md`，还缺少以下关键内容：

1. **项目定位不清晰**：没有说明这是 API 服务、前端应用，还是提示词/评测仓库。
2. **缺少启动方式**：新成员无法快速运行或验证项目是否正常。
3. **缺少开发规范**：没有代码风格、分支命名、提交规范与测试要求。
4. **缺少质量保障说明**：没有测试、Lint、CI/CD 的描述。
5. **缺少路线图**：看不到下一步要做什么，难以协作推进。

## 建议的下一步（按优先级）

### P0（建议本周完成）
- 补齐项目基础目录（如 `src/`、`tests/`、`docs/`）。
- 增加 `CONTRIBUTING.md`（开发流程）和 `CHANGELOG.md`（版本记录）。
- 增加最小可运行示例（例如一个 `hello chatbot` 服务或 CLI）。

### P1（建议 1~2 周内完成）
- 接入基础质量检查（例如：格式化 + Lint + 单元测试）。
- 新增 GitHub Actions 工作流：PR 自动检查。
- 建立 `docs/architecture.md`，记录模块边界和数据流。

### P2（建议后续迭代）
- 增加评测基线（准确率、响应时延、幻觉率等指标）。
- 增加 prompt/agent 的版本化策略。
- 增加观测与告警（日志结构化、错误码、追踪链路）。

## 可参考的最小目录结构

```text
.
├─ README.md
├─ src/
│  └─ main.(py|ts|go)
├─ tests/
│  └─ test_smoke.*
├─ docs/
│  └─ architecture.md
├─ .github/workflows/
│  └─ ci.yml
├─ CONTRIBUTING.md
└─ CHANGELOG.md
```

## 你可以马上做的 3 件事

1. 明确项目目标（例如“一个支持工具调用的客服 chatbot API”）。
2. 选定技术栈并补一个最小可运行 Demo。
3. 配置 CI：至少保证 PR 时能自动跑格式化和测试。

---

如果你愿意，我下一步可以直接帮你：
- 生成一个可运行的最小 chatbot 模板（Python 或 Node.js 二选一）；
- 一次性补齐 `CONTRIBUTING.md`、`CHANGELOG.md`、CI 配置；
- 加上基础测试与本地开发脚本。
