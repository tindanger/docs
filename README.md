# Mintlify Starter Kit

Click on `Use this template` to copy the Mintlify starter kit. The starter kit contains examples including

* Guide pages

* Navigation

* Customizations

* API Reference pages

* Use of popular components

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where docs.json is)

```
mintlify dev
```

### Publishing Changes

Install our Github App to auto propagate changes from your repo to your deployment. Changes will be deployed to production automatically after pushing to the default branch. Find the link to install on your dashboard.

#### Troubleshooting

├── docs/
│   └── UserGuide/          <—— 当前文件夹
│       ├── quick-start.mdx  <—— 当前文件
│   └── Terms/          <—— 目标文件夹
│       ├── Enterprise_Certification_User_Agreement_JQB.mdx
│       └── ...
